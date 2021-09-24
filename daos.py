from db import DB
from typing import List, Tuple

class CryptoDAO(DB):
    """Class for handling database interactions for top_crypto_currencies table"""
    TABLE_NAME = 'top_crypto_currencies'

    def __init__(self) -> None:
        self.create_tables()

    def create_tables(self) -> None:
        with self.get_cursor(self.get_connection()) as cursor:
            sql = f"""CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                    id INT(11) AUTO_INCREMENT PRIMARY KEY,
                    symbol VARCHAR(10) NOT NULL,
                    name VARCHAR(45) NOT NULL,
                    current_price DECIMAL(14,6),
                    `rank` INT(11) NOT NULL,
                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )"""
            cursor.execute(sql)

    def insert_many(self, data: List[Tuple]) -> None:
        with self.get_cursor(self.get_connection()) as cursor:
            sql = f"""INSERT INTO {self.TABLE_NAME} (symbol, name, current_price, `rank`) VALUES (%s, %s, %s, %s)"""
            cursor.executemany(sql, data)


crypto_dao = CryptoDAO()
