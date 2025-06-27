import mysql.connector
from mysql.connector import Error

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "521996RRrr##"
TARGET_DB = "alx_book_store"

def main():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {alx_book_store};")
            connection.commit()

            print(f"Database '{alx_book_store}' created successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()
