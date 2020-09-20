import psycopg2

from core.config import DATABASE_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from core.log import logger


class DataBase:
    def __init__(self):

        logger.info("Database Init")
        self.__connect_to_db()

    def __connect_to_db(self):

        self.pool_min_connections = MIN_CONNECTIONS_COUNT
        self.pool_max_connections = MAX_CONNECTIONS_COUNT

        logger.info("Attempting DB connection")

        self.db_conn = psycopg2.connect(DATABASE_URL)
        self.db_conn.autocommit = True

        logger.debug("DB Conn Params", conn=self.db_conn.dsn)
        logger.info("DB connected")


    def get_database_connection(self):

        # Read-only integer attribute:
        # 0 if the connection is open
        # nonzero if it is closed or broken
        conn_status = self.db_conn.closed
        logger.debug("DB connection status", connection_status=conn_status)

        if conn_status:
            logger.info("DB is not connected - reconnecting")
            self.__connect_to_db()

        return self.db_conn

    def disconnect_from_database():
        logger.info("Closing DB connection")
        self.db_conn.close()
        logger.info("Closed DB connection")