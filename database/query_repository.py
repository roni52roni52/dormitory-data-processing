class QueryRepository:
    def __init__(self, connection):
        # Store the database connection
        self.connection = connection

    def get_rooms_with_student_count(self):

        # SQL query that returns every room and its number of students
        query = """
            SELECT
                r.id,
                r.name,
                COUNT(s.id) AS student_count
            FROM rooms AS r
            LEFT JOIN students AS s
                ON r.id = s.room_id
            GROUP BY r.id, r.name
            ORDER BY r.id
        """

        # Create a dictionary cursor so results contain column names
        cursor = self.connection.cursor(dictionary=True)

        try:
            # Execute the SQL query
            cursor.execute(query)

            # Return all query results
            return cursor.fetchall()

        finally:
            # Always close the cursor
            cursor.close()

    def get_rooms_with_lowest_average_age(self):

        # SQL query that returns 5 rooms with the lowest average student age
        query = """
            SELECT
                r.id,
                r.name,
                AVG(TIMESTAMPDIFF(DAY, s.birthday, CURDATE())) / 365.2425
                    AS average_age
            FROM rooms AS r
            INNER JOIN students AS s
                ON r.id = s.room_id
            GROUP BY r.id, r.name
            ORDER BY average_age ASC
            LIMIT 5
        """

        # Create a dictionary cursor so results contain column names
        cursor = self.connection.cursor(dictionary=True)

        try:
            # Execute the SQL query
            cursor.execute(query)

            # Return all query results
            return cursor.fetchall()

        finally:
            # Always close the cursor
            cursor.close()

    def get_rooms_with_largest_age_difference(self):

        # SQL query that returns 5 rooms with the largest student age difference
        query = """
            SELECT
                r.id,
                r.name,
                TIMESTAMPDIFF(
                    DAY,
                    MIN(s.birthday),
                    MAX(s.birthday)
                ) / 365.2425 AS age_difference
            FROM rooms AS r
            INNER JOIN students AS s
                ON r.id = s.room_id
            GROUP BY r.id, r.name
            HAVING COUNT(s.id) >= 2
            ORDER BY age_difference DESC
            LIMIT 5
        """

        # Create a dictionary cursor so results contain column names
        cursor = self.connection.cursor(dictionary=True)

        try:
            # Execute the SQL query
            cursor.execute(query)

            # Return all query results
            return cursor.fetchall()

        finally:
            # Always close the cursor
            cursor.close()
    def get_rooms_with_different_sexes(self):

        # SQL query that returns rooms with students of different sexes
        
        query = """
            SELECT
                r.id,
                r.name
            FROM rooms AS r
            INNER JOIN students AS s
                ON r.id = s.room_id
            GROUP BY r.id, r.name
            HAVING COUNT(DISTINCT s.sex) > 1
            ORDER BY r.id
        """

        # Create a dictionary cursor so results contain column names
        cursor = self.connection.cursor(dictionary=True)

        try:
            # Execute the SQL query
            cursor.execute(query)

            # Return all query results
            return cursor.fetchall()

        finally:
            # Always close the cursor
            cursor.close()