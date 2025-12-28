import mysql.connector.pooling
from config import DB_CONFIG

class DBConnection:
    _pool = None

    @classmethod
    def get_connection(cls):
        if cls._pool is None:
            cls._pool = mysql.connector.pooling.MySQLConnectionPool(**DB_CONFIG)
        return cls._pool.get_connection()