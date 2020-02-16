import os
import random

from core.config import QUOTE_BACKEND

if QUOTE_BACKEND == 'DB':
    from crud.quotes_db import get_quote_random
else:
    from crud.quotes_list import get_quote_random


def get_quote():
    
    quote = get_quote_random()
    return quote
