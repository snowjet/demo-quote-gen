import os
import pathlib

from dotenv import load_dotenv
from core.security import decrypt
from core.log import logger


from pydantic import BaseSettings
from pydantic import BaseModel, HttpUrl, ValidationError


class Settings(BaseSettings):
    PROJECT_NAME: str = "Backend Application"
    log_level: str = "INFO"
    external_image_api: HttpUrl = "http://127.0.0.1:8001/api/v1/image"
    external_image_api_v2: HttpUrl = "http://127.0.0.1:8001/api/v2/image"

    class Config:
        env_file = ".env"


settings = Settings()


env_file = os.environ.get("env_file", ".env")
load_dotenv(env_file)

PROJECT_NAME = os.getenv("PROJECT_NAME", "app")
QUOTE_BACKEND = os.getenv("QUOTE_BACKEND", "LIST")
DATABASE_URL = os.getenv("DATABASE_URL", "")

if not DATABASE_URL:
    DATABASE_TYPE = os.getenv("DATABASE_TYPE", "sqlite").lower()
    if DATABASE_TYPE in ["sqlite", "postgresql", "mysql"]:

        logger.info("Using Database Type " + DATABASE_TYPE, type=DATABASE_TYPE)
    else:
        logger.info("Incorrect Databse Type provided using sqlite", type=DATABASE_TYPE)
        DATABASE_TYPE = "sqlite"

    SQLITE_FILE_PATH = os.getenv("SQLITE_FILE_PATH", "./sql_app.db")
    DATABASE_HOST = os.getenv("DATABASE_SERVICE_HOST", "127.0.0.1")
    DATABASE_USER = os.getenv("database-user", "user")
    DATABASE_PASS = os.getenv("database-password", "postgres")
    DATABASE_NAME = os.getenv("database-name", "quotes")

    if DATABASE_TYPE == "sqlite":
        SQLALCHEMY_DATABASE_URL = "sqlite:///%s" % (SQLITE_FILE_PATH)
    else:
        SQLALCHEMY_DATABASE_URL = "%s://%s:%s@%s/%s" % (
            DATABASE_TYPE,
            DATABASE_USER,
            DATABASE_PASS,
            DATABASE_HOST,
            DATABASE_NAME,
        )
else:
    SQLALCHEMY_DATABASE_URL = DATABASE_URL

logger.debug("Database URL " + SQLALCHEMY_DATABASE_URL, SQLALCHEMY_DATABASE_URL=SQLALCHEMY_DATABASE_URL)

json_file_path = None
if os.getenv("JSON_QUOTE_PATH", None) is not None:
    test_env_path = pathlib.Path(os.getenv("JSON_QUOTE_PATH"))

    if test_env_path.is_file():
        json_file_path = test_env_path
