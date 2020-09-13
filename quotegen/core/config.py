import os
import pathlib

from dotenv import load_dotenv
from core.security import decrypt

env_file = os.environ.get("env_file", ".env")
load_dotenv(env_file)

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
PROJECT_NAME = os.getenv("PROJECT_NAME", "app")
QUOTE_BACKEND = os.getenv("QUOTE_BACKEND", "LIST")
DATABASE_URL = os.getenv("DATABASE_URL", "")

"""Test if Database Schema path is valid and exists"""
DB_SCHEMA_PATH = pathlib.Path.cwd().joinpath("db", "db_schema", "initdb.sql")
if os.getenv("DB_SCHEMA_PATH", None) is not None:
    test_db_env_path = pathlib.Path(os.getenv("DB_SCHEMA_PATH"))

    if test_db_env_path.is_file():
        DB_SCHEMA_PATH = test_db_env_path

if not DATABASE_URL:
    POSTGRES_HOST = os.getenv("POSTGRESQL_SERVICE_HOST", "127.0.0.1")
    POSTGRES_PORT = int(os.getenv("POSTGRES_SERVICE_PORT", 5432))
    POSTGRES_USER = os.getenv("database-user", "postgres")
    POSTGRES_PASS = os.getenv("database-password", "postgres")
    POSTGRES_NAME = os.getenv("database-name", "quotes")

    DATABASE_URL = f"host='{POSTGRES_HOST}' port='{POSTGRES_PORT}' dbname='{POSTGRES_NAME}' user='{POSTGRES_USER}' password='{POSTGRES_PASS}'"

# Placeholder for connection pooling
MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))

print("Reading OS")
print(os.getenv("JSON_QUOTE_PATH", None))
json_file_path = pathlib.Path.cwd().joinpath("quotes", "quotes.json")
if os.getenv("JSON_QUOTE_PATH", None) is not None:
    test_env_path = pathlib.Path(os.getenv("JSON_QUOTE_PATH"))
    print(test_env_path)

    if test_env_path.is_file():
        json_file_path = test_env_path
