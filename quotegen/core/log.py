import logging
import os
import daiquiri

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
if LOG_LEVEL not in ["INFO", "DEBUG"]:
    LOG_LEVEL = "INFO"

class quotelogging:
    def __init__(self):

        daiquiri.setup(level=LOG_LEVEL)
        self.logger = daiquiri.getLogger(__name__)

    def get_logger(self):

        return self.logger


daiquiri.setup(level=LOG_LEVEL)
logger = daiquiri.getLogger(__name__)
