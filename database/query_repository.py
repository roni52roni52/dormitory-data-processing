from mysql.connector.abstracts import MySQLConnectionAbstract


class QueryRepository:
    def __init__(
        self,
        connection: MySQLConnectionAbstract,
    ) -> None:
        self.connection = connection

    def get_rooms_with_student_count(self) -> list[dict]:
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

        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_rooms_with_lowest_average_age(self) -> list[dict]:
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

        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_rooms_with_largest_age_difference(self) -> list[dict]:
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

        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_rooms_with_different_sexes(self) -> list[dict]:
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

        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            return cursor.fetchall()