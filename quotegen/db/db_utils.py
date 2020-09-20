import os

import psycopg2

from core.log import logger
from core.config import DB_SCHEMA_PATH
from db.database import DataBase

logger.info("Get DB instance")
db = DataBase()


def get_database_connection():

    db_conn = db.get_database_connection()
    
    return db_conn


def disconnect_from_database():
    logger.info("Closing DB connection")
    db.disconnect_from_database()
    logger.info("Closed DB connection")


def load_schema_safe():

    db_conn = get_database_connection()
    db_conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = db_conn.cursor()

    # First check if postgres already has a schema
    cursor.execute(
        "SELECT EXISTS ( SELECT 1 \
                    FROM   pg_tables \
                    WHERE  schemaname = 'public' \
                    AND    tablename = 'quotes' \
                    );"
    )

    table_exists = cursor.fetchall()

    if not table_exists[0][0]:
        return_msg = "Schema Not Found - Adding schema"
        logger.info(return_msg)

        sql_file = open(DB_SCHEMA_PATH, "r")
        cursor.execute(sql_file.read())
    else:
        return_msg = "tables already has a schema"
        logger.info(return_msg)

    cursor.close()

    return return_msg
