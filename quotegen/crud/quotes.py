from sqlalchemy.orm import Session
from sqlalchemy.orm import load_only, deferred


from db import models, schemas
from core.log import logger

import random


def check_quote(quote=None):
    if quote is not None:
        return {"name": quote.name, "quote": quote.quote}
    else:
        return "no results"


def get_quote_by_id(db: Session, id: int):
    quote = db.query(models.Quotes).filter(models.Quotes.id == id).first()
    return check_quote(quote)


def delete_quote_by_id(db: Session, id: int):
    quote = db.query(models.Quotes).filter(models.Quotes.id == id).first()
    return check_quote(quote)


def get_quote_by_name(db: Session, name: str):
    quote = db.query(models.Quotes).filter(models.Quotes.name == name).first()
    return check_quote(quote)


def delete_quotes_by_name(db: Session, name: str):
    quote = db.query(models.Quotes).filter(models.Quotes.name == name).first()
    return check_quote(quote)


def delete_all_quotes(db: Session):
    logger.info("Deleting all entries")
    db.query(models.Quotes).delete()
    db.commit()
    return "all entries deleted"


def get_quote_by_name_and_quote(db: Session, name: str, quote: str):
    quote = (
        db.query(models.Quotes)
        .filter(models.Quotes.name == name, models.Quotes.quote == quote)
        .first()
    )
    return check_quote(quote)


def get_all_quotes(db: Session, skip: int = 0, limit: int = 100):
    quotes = db.query(models.Quotes).offset(skip).limit(limit).all()
    quote_list = []
    for quote in quotes:
        quote = check_quote(quote)
        quote_list.append(quote)

    return quote_list


def get_all_quotes_with_id(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quotes).offset(skip).limit(limit).all()


def get_all_quotes_with_ids(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quotes).offset(skip).limit(limit).all()


def get_random_quote(db: Session):
    query = db.query(models.Quotes).options(load_only("name", "quote"))
    rowCount = int(query.count())
    quote = query.offset(int(rowCount * random.random())).first()
    return check_quote(quote)


def create_quote(db: Session, quote: schemas.QuotesCreate):
    db_quote = models.Quotes(name=quote.name, quote=quote.quote)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote


def seed_db(db: Session, quoteList: schemas.QuotesList):
    if db.query(models.Quotes).first() is None:
        for quote in quoteList.quotes:
            create_quote(db=db, quote=quote)

        logger.info("database successfully seeded")
        logger.debug("databse seesed with", quote=quoteList)

        return True

    return None
