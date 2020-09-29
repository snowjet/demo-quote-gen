from sqlalchemy.orm import Session

from db import models, schemas
from core.log import logger
import json


def get_quote_by_id(db: Session, quote_id: int):
    return db.query(models.Quotes).filter(models.Quotes.id == quote_id).first()


def get_quote_by_name(db: Session, name: str):
    return db.query(models.Quotes).filter(models.Quotes.name == name).first()


def get_quote_by_name_and_quote(db: Session, name: str, quote: str):
    return (
        db.query(models.Quotes)
        .filter(models.Quotes.name == name, models.Quotes.quote == quote)
        .first()
    )


def get_quotes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quotes).offset(skip).limit(limit).all()


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
