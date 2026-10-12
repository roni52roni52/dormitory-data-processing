from datetime import datetime


class StudentRepository:
    def __init__(self, connection):
        # Store the database connection
        self.connection = connection

    def delete_all(self):
        try:
            # Use a context manager to ensure the cursor is always closed
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM students")

            # Save changes in the database
            self.connection.commit()

        except Exception:
            # Undo uncommitted changes and propagate the error
            self.connection.rollback()
            raise

    def insert_many(self, students):
        # SQL query used to insert students into the database
        query = """
            INSERT INTO students (id, name, birthday, sex, room_id)
            VALUES (%s, %s, %s, %s, %s)
        """

        # Prepare values and convert birthday strings to datetime objects
        values = [
            (
                student["id"],
                student["name"],
                datetime.fromisoformat(student["birthday"]),
                student["sex"],
                student["room"],
            )
            for student in students
        ]

        # Create a cursor for executing SQL queries
        cursor = self.connection.cursor()

        try:
            # Insert all students using a single batch operation
            cursor.executemany(query, values)

            # Save changes in the database
            self.connection.commit()

        except Exception:
            # Undo changes if something goes wrong
            self.connection.rollback()
            raise

        finally:
            # Always close the cursor
            cursor.close()