import json
import pathlib
from core.log import logger


def return_json_quotes(filepath):

    logger.debug("Reading JSON Quotes from file")
    with open(filepath, mode="r") as fid:
        quotes_as_json = json.load(fid)

    logger.debug("JSON quotes from file", file=quotes_as_json)

    return quotes_as_json
