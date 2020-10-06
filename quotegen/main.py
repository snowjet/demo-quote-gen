from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import List

from fastapi import Depends, FastAPI, HTTPException

from core.config import json_file_path
from core.log import logger

from sqlalchemy.orm import Session

from crud import quotes as quotesCRUD
from crud import images as imagesCRUD
from crud.read_json import return_json_quotes
from db import models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

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


def add_backend(fieldname: str = "detail", msg: str = None):

    content = {}
    content["backend"] = sql_drivername
    content[fieldname] = msg

    return content


""" Bootstrap the DB if enviornment path to file is provided """
if json_file_path is not None:
    quotes_as_json = return_json_quotes(json_file_path)

    logger.debug("attempting to seed DB")
    db_session = SessionLocal()

    quoteList = schemas.QuotesList(quotes=quotes_as_json["quotes"])
    if quotesCRUD.seed_db(db=db_session, quoteList=quoteList) is None:
        logger.info("DB Seed Unsuccessful")
    else:
        logger.info("database successfully seeded")

    db_session.close()


@app.get("/", response_model=List[schemas.Quote])
async def quote(db: Session = Depends(get_db)):

    quote = jsonable_encoder(quotesCRUD.get_random_quote(db))
    content = add_backend(fieldname="quotes", msg=quote)

    return JSONResponse(content=content)


@app.get("/quotes", response_model=List[schemas.Quote])
async def list_quotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    quote = jsonable_encoder(quotesCRUD.get_all_quotes(db, skip=skip, limit=limit))
    content = add_backend(fieldname="quotes", msg=quote)

    return JSONResponse(content=content)


@app.get("/quotes/id", response_model=List[schemas.Quote])
async def get_all_quotes_with_id(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    quote = jsonable_encoder(quotesCRUD.get_all_quotes_with_id(db, skip=skip, limit=limit))
    content = add_backend(fieldname="quotes", msg=quote)

    return JSONResponse(content=content)


@app.get("/quote/id/{id}", response_model=List[schemas.Quote])
async def get_quote(id: int, db: Session = Depends(get_db)):

    quote = jsonable_encoder(quotesCRUD.get_quote_by_id(db, id=id))
    content = add_backend(fieldname="quotes", msg=quote)

    return JSONResponse(content=content)


@app.get("/quote/name/{name}", response_model=List[schemas.Quote])
async def get_quote(name: str, db: Session = Depends(get_db)):

    quote = jsonable_encoder(quotesCRUD.get_quote_by_name(db, name=name))
    content = add_backend(fieldname="quotes", msg=quote)

    return JSONResponse(content=content)


@app.get("/quote/image", response_model=List[schemas.Quote])
async def get_image(name: str):

    image = jsonable_encoder(imagesCRUD.get_image_simple(apiVersion=1, name=name))
    return JSONResponse(content=image)


@app.post("/quote", response_model=schemas.Quote)
def create_quote(quote: schemas.QuotesCreate, db: Session = Depends(get_db)):
    db_quote = quotesCRUD.get_quote_by_name_and_quote(
        db, name=quote.name, quote=quote.quote
    )
    if db_quote:
        raise HTTPException(status_code=400, detail="Quote Already Exists")

    quote = jsonable_encoder(quotesCRUD.create_quote(db=db, quote=quote))
    content = add_backend(fieldname="quotes", msg=quote)

    return JSONResponse(content=content)


@app.post("/seed", response_model=schemas.QuotesList)
def seed_db(quoteList: schemas.QuotesList, db: Session = Depends(get_db)):
    if quotesCRUD.seed_db(db=db, quoteList=quoteList) is None:
        raise HTTPException(status_code=400, detail="DB Seed Unsuccessful")

    msg = "database successfully seeded"
    content = add_backend(fieldname="detail", msg=msg)

    return JSONResponse(content=content)


@app.get("/admin/delete_all", response_model=List[schemas.Quote])
async def delete_all_quotes(db: Session = Depends(get_db)):

    msg = jsonable_encoder(quotesCRUD.delete_all_quotes(db))
    content = add_backend(fieldname="detail", msg=msg)

    return JSONResponse(content=content)
