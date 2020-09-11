import os
import random

from itertools import chain
from core.config import QUOTE_BACKEND

if QUOTE_BACKEND == "DB":
    from crud.quotes_db import QuoteDB
    quotes = QuoteDB()
    backend = "Database"
else:
    from crud.quotes_list import QuotesList
    quotes = QuotesList()
    backend = "list"

defaults = ["error", "error"]


def get_quote():

    name, quote, *_ = chain(quotes.get_quote_random(), defaults)

    return name, quote, backend
