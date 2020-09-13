from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from core.config import LOG_LEVEL, QUOTE_BACKEND
from core.log import logger
from core.quote import get_quote

logger.info("Config Imported", LOG_LEVEL=LOG_LEVEL)

if LOG_LEVEL == "DEBUG":
    DEBUG = True
else:
    DEBUG = False

app = FastAPI()

if QUOTE_BACKEND == "DB":
    from db.db_utils import load_schema_safe

    msg = load_schema_safe()
    logger.info("Setup DB", load_schema_msg=msg)


@app.get("/")
async def home():
    name, quote, backend = get_quote()
    msg_dict = {"name": name, "quote": quote, "backend": backend}
    msg = jsonable_encoder(msg_dict)
    logger.info("Returned Quote:", qoute=msg_dict)
    return JSONResponse(content=msg)
