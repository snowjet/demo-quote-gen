from core.log import logger
from db.db_utils import get_database_connection

db_conn = get_database_connection()


def get_quotes():
    """Returns a dict of quotes"""

    cursor = db_conn.cursor()

    cursor.execute(
        "SELECT * from quotes;")
        
    quotes = cursor.fetchall()

    # Close communication with the database
    cursor.close()

    return quotes


def get_quote_random():
    """Returns a dict of quotes"""

    cursor = db_conn.cursor()

    cursor.execute(
        "select name,quote from quotes OFFSET floor(random()*(select count(*)from quotes)) LIMIT 1;")
        
    quote = cursor.fetchone()

    # Close communication with the database
    cursor.close()

    return quote


