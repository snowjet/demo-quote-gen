import os
import random

from core.config import json_file_path
from crud.read_json import return_json_quotes
from core.log import logger


class QuotesList:
    def __init__(self):
        self.quotes_list = return_json_quotes(json_file_path)

    def get_quote_random(self):
        if not "quotes" in self.quotes_list or len(self.quotes_list["quotes"]) == 0:
            self.quotes_list = return_json_quotes(json_file_path)
            logger.info("JSON Quote List Empty Import Quotes from filesystem")

        index = int(random.randint(0, len(self.quotes_list["quotes"]) - 1))

        return (
            self.quotes_list["quotes"][index]["name"],
            self.quotes_list["quotes"][index]["quote"],
        )
