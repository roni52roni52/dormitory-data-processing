from config import DB_CONFIG
from database.connection import DatabaseConnection
from loaders.json_loader import JsonLoader
from database.room_repository import RoomRepository
from database.student_repository import StudentRepository
from database.query_repository import QueryRepository
from exporters.json_exporter import JsonExporter
from exporters.xml_exporter import XmlExporter
import argparse


def parse_arguments():

    # Create command-line argument parser
    parser = argparse.ArgumentParser(
        description="Dormitory data processing application"
    )

    # Path to the students JSON file
    parser.add_argument(
        "--students",
        required=True,
        help="Path to the students JSON file",
    )

    # Path to the rooms JSON file
    parser.add_argument(
        "--rooms",
        required=True,
        help="Path to the rooms JSON file",
    )

    # Output format
    parser.add_argument(
        "--format",
        required=True,
        choices=["json", "xml"],
        help="Output format: json or xml",
    )

    return parser.parse_args()

def main():
    # Read command-line arguments
    args = parse_arguments()

    # Create a connection to the MySQL database using configuration settings
    database = DatabaseConnection(**DB_CONFIG)

    try:
        # Confirm that the database connection was established successfully
        print("Connected to MySQL")

        # Create a JSON loader
        loader = JsonLoader()

        # Load data from files provided through command-line arguments
        rooms = loader.load(args.rooms)
        students = loader.load(args.students)

        # Display the number of loaded records
        print("Rooms loaded:", len(rooms))
        print("Students loaded:", len(students))

        # Create repositories for database operations
        room_repository = RoomRepository(database.get_connection())
        student_repository = StudentRepository(database.get_connection())

        # Remove previously imported data
        # Students must be deleted first because they reference rooms
        student_repository.delete_all()
        room_repository.delete_all()

        # Insert rooms first because students reference rooms
        room_repository.insert_many(rooms)

        # Insert students after all rooms have been inserted
        student_repository.insert_many(students)

        print("Data inserted successfully")

        # Create a repository for analytical queries
        query_repository = QueryRepository(database.get_connection())

        # Get rooms with the number of students in each room
        rooms_with_student_count = (
            query_repository.get_rooms_with_student_count()
        )

        # Get 5 rooms with the lowest average student age
        rooms_with_lowest_average_age = (
            query_repository.get_rooms_with_lowest_average_age()
        )

        # Get 5 rooms with the largest student age difference
        rooms_with_largest_age_difference = (
            query_repository.get_rooms_with_largest_age_difference()
        )

        # Get rooms where students of different sexes live
        rooms_with_different_sexes = (
            query_repository.get_rooms_with_different_sexes()
        )

        # Collect all query results
        results = {
            "rooms_with_student_count": rooms_with_student_count,
            "rooms_with_lowest_average_age": rooms_with_lowest_average_age,
            "rooms_with_largest_age_difference": rooms_with_largest_age_difference,
            "rooms_with_different_sexes": rooms_with_different_sexes,
        }

        # Export query results in the selected format
        if args.format == "json":
            exporter = JsonExporter()
            output_file = "results.json"
        else:
            exporter = XmlExporter()
            output_file = "results.xml"

        exporter.export(results, output_file)

        print(f"Results exported to {output_file}")

    finally:
        # Always close the database connection
        database.close()

# Run the main function only when this file is executed directly
if __name__ == "__main__":
    main()