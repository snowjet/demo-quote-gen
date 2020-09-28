from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import List

from fastapi import Depends, FastAPI, HTTPException

from core.config import LOG_LEVEL
from core.log import logger

from sqlalchemy.orm import Session

from crud import quotes as crud
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
    try:
        yield db_session
    finally:
        db_session.close()

    logger.info("Setup DB")


def add_backend(quote):

    content = []
    content.append({"backend": sql_drivername})
    content.append({"quotes": quote})

    return content


@app.get("/", response_model=List[schemas.Quote])
async def home(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    quote = jsonable_encoder(crud.get_quotes(db, skip=skip, limit=limit))
    content = add_backend(quote)

    return JSONResponse(content=content)


@app.get("/quotes", response_model=List[schemas.Quote])
async def list_quotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # name, quote, backend = get_quote()
    # msg_dict = {"name": name, "quote": quote, "backend": backend}
    # msg = jsonable_encoder(msg_dict)

    return add_backend(crud.get_quotes(db, skip=skip, limit=limit))


@app.post("/quote/", response_model=schemas.Quote)
def create_quote(quote: schemas.QuotesCreate, db: Session = Depends(get_db)):
    db_quote = crud.get_quote_by_name_and_quote(db, name=quote.name, quote=quote.quote)
    if db_quote:
        raise HTTPException(status_code=400, detail="Quote Already Exists")

    quote = jsonable_encoder(crud.create_quote(db=db, quote=quote))
    content = add_backend(quote)

    return JSONResponse(content=content)
