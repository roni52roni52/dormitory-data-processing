from mysql.connector.abstracts import MySQLConnectionAbstract


class RoomRepository:
    def __init__(
        self,
        connection: MySQLConnectionAbstract,
    ) -> None:
        # Store the database connection
        self.connection = connection

    def delete_all(self) -> None:
        try:
            # Open a cursor using a context manager
            with self.connection.cursor() as cursor:
                # Remove all existing rooms from the database
                cursor.execute("DELETE FROM rooms")

            # Save changes in the database
            self.connection.commit()

        except Exception:
            # Undo changes if something goes wrong
            self.connection.rollback()
            raise

    def insert_many(
        self,
        rooms: list[dict[str, int | str]],
    ) -> None:
        # SQL query used to insert rooms into the database
        query = """
            INSERT INTO rooms (id, name)
            VALUES (%s, %s)
        """

        # Prepare room values for the INSERT query
        values = []

        for room in rooms:
            values.append(
                (room["id"], room["name"])
            )

        try:
            # Open a cursor using a context manager
            with self.connection.cursor() as cursor:
                # Insert all rooms
                cursor.executemany(query, values)

            # Save changes in the database
            self.connection.commit()

        except Exception:
            # Undo changes if something goes wrong
            self.connection.rollback()
            raise