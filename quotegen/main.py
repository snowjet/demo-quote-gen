from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import List

from fastapi import Depends, FastAPI, HTTPException

from core.config import LOG_LEVEL, json_file_path
from core.log import logger

from sqlalchemy.orm import Session

from crud import quotes as quotesCRUD
from crud.read_json import return_json_quotes
from db import models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

logger.info("Config Imported", LOG_LEVEL=LOG_LEVEL)

if LOG_LEVEL == "DEBUG":
    DEBUG = True
else:
    DEBUG = False

app = FastAPI()
sql_drivername = str(engine.url.drivername)


def get_db():

    db_session = SessionLocal()
    logger.debug("DB session obtained")
    try:
        yield db_session
    finally:
        db_session.close()
        logger.debug("DB Closed")


def add_backend(quote):

    content = []
    content.append({"backend": sql_drivername})
    content.append({"quotes": quote})

    return content


""" Bootstrap the DB if enviornment path to file is provided """
print(json_file_path)
if json_file_path is not None:
    quotes_as_json = return_json_quotes(json_file_path)

    logger.debug("attempting to seed DB")
    db_session = SessionLocal()

    quoteList = schemas.QuotesList(quotes=quotes_as_json["quotes"])
    if quotesCRUD.seed_db(db=db_session, quoteList=quoteList) is None:
        logger.info("DB Seed Unsuccessful")

    db_session.close()
    logger.info("database successfully seeded")


@app.get("/", response_model=List[schemas.Quote])
async def home(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    quote = jsonable_encoder(quotesCRUD.get_quotes(db, skip=skip, limit=limit))
    content = add_backend(quote)

    return JSONResponse(content=content)


@app.get("/quotes", response_model=List[schemas.Quote])
async def list_quotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    quote = jsonable_encoder(quotesCRUD.get_quotes(db, skip=skip, limit=limit))
    content = add_backend(quote)

    return JSONResponse(content=content)


@app.post("/quote", response_model=schemas.Quote)
def create_quote(quote: schemas.QuotesCreate, db: Session = Depends(get_db)):
    db_quote = quotesCRUD.get_quote_by_name_and_quote(
        db, name=quote.name, quote=quote.quote
    )
    if db_quote:
        raise HTTPException(status_code=400, detail="Quote Already Exists")

    quote = jsonable_encoder(quotesCRUD.create_quote(db=db, quote=quote))
    content = add_backend(quote)

    return JSONResponse(content=content)


@app.post("/seed", response_model=schemas.QuotesList)
def seed_db(quoteList: schemas.QuotesList, db: Session = Depends(get_db)):
    if quotesCRUD.seed_db(db=db, quoteList=quoteList) is None:
        raise HTTPException(status_code=400, detail="DB Seed Unsuccessful")

    content = {"detail": "database successfully seeded"}
    return JSONResponse(content=content)
