class RoomRepository:
    def __init__(self, connection):
        # Store the database connection
        self.connection = connection

    def delete_all(self):
        # Create a cursor for executing SQL queries
        cursor = self.connection.cursor()

        try:
            # Remove all existing rooms from the database
            cursor.execute("DELETE FROM rooms")

            # Save changes in the database
            self.connection.commit()

        except Exception:
            # Undo changes if something goes wrong
            self.connection.rollback()
            raise

        finally:
            # Always close the cursor
            cursor.close()

    def insert_many(self, rooms):
        # SQL query used to insert rooms into the database
        query = """
            INSERT INTO rooms (id, name)
            VALUES (%s, %s)
        """

        # Convert room dictionaries into tuples expected by MySQL
        values = [
            (room["id"], room["name"])
            for room in rooms
        ]

        # Create a cursor for executing SQL queries
        cursor = self.connection.cursor()

        try:
            # Insert all rooms using a single batch operation
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