import os
from contextlib import contextmanager
import pymysql.cursors
from pymysql.err import MySQLError
from errors import DatabaseError

class DB:
    """Class instantiating database connections"""

    def get_connection(self):
        return pymysql.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'),
                db=os.getenv('DB_DATABASE'),
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

    @contextmanager
    def get_cursor(self, connection):
        cursor = connection.cursor()
        try:
            yield cursor
            connection.commit()
        except MySQLError as e:
            raise DatabaseError(f"Database error: {e}")
        finally:
            cursor.close()
            connection.close()