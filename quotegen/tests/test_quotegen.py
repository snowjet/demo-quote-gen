import pytest

from fastapi.testclient import TestClient
import os
import pathlib
import pytest

json_file_path = str(pathlib.Path.cwd().joinpath("tests", "quotes", "quotes.json"))
os.environ.update({"JSON_QUOTE_PATH": json_file_path})

from crud.read_json import return_json_quotes
from main import app
from core.log import logger

test_quotes_list = return_json_quotes(json_file_path)
client = TestClient(app)


def test_get_quotes():

    logger.info("Running '/' tests")

    logger.info("Get '/admin/delete_all'")
    response = client.get("/admin/delete_all")

    logger.info("Post '/seed'")
    response = client.post("/seed", json=test_quotes_list)

    logger.info("Get '/'")
    response = client.get("/")
    assert response.status_code == 200

    msg = response.json()
    del msg["backend"]
    logger.info("Quote Received " + str(msg["quotes"]))

    if msg["quotes"] not in test_quotes_list["quotes"]:
        assert False


def test_get_quotes():

    logger.info("Running '/quotes' tests")

    logger.info("Get '/admin/delete_all'")
    response = client.get("/admin/delete_all")

    logger.info("Post '/seed'")
    response = client.post("/seed", json=test_quotes_list)

    logger.info("Get '/quotes'")
    response = client.get("/quotes")
    assert response.status_code == 200

    msg = response.json()
    del msg["backend"]
    logger.info("Quote Received " + str(msg["quotes"]))

    for quote in msg["quotes"]:
        if quote not in test_quotes_list["quotes"]:
            print(quote)
            assert False


def test_get_quote_by_id():

    logger.info("Running '/quote/id/{id}' tests")

    logger.info("Get '/admin/delete_all'")
    response = client.get("/admin/delete_all")

    logger.info("Post '/seed'")
    response = client.post("/seed", json=test_quotes_list)

    logger.info("Get '/quotes/id'")
    response = client.get("/quotes/id")
    msg = response.json()

    quote_ids = []
    for quote in msg['quotes']:
        quote_ids.append(quote['id'])
    
    logger.debug("List of quote_ids", quote_ids=quote_ids)

    size_of_quotes = len(test_quotes_list['quotes'])
    for id in quote_ids:
        logger.info("Get '/quote/id/" + str(id) + "'")
        response = client.get("/quote/id/" + str(id))
        assert response.status_code == 200

        msg = response.json()
        del msg["backend"]
        logger.info("Quote Received " + str(msg["quotes"]))

        if msg["quotes"] not in test_quotes_list["quotes"]:
            assert False


def test_get_quote_by_name():

    logger.info("Running '/quote/name/{name}' tests")

    logger.info("Get '/admin/delete_all'")
    response = client.get("/admin/delete_all")

    logger.info("Post '/seed'")
    response = client.post("/seed", json=test_quotes_list)

    for quote in test_quotes_list['quotes']:
        logger.info("Get '/quote/name/" + quote['name'] + "'")
        response = client.get("/quote/name/" + quote['name'] )
        assert response.status_code == 200

        msg = response.json()
        del msg["backend"]
        logger.info(str(quote))
        logger.info("Quote Received " + str(msg["quotes"]))

        if msg["quotes"] != quote:
            assert False


def test_delete_quote_by_name():

    logger.info("Running '/quote/name/{name}' tests")

    logger.info("Get '/admin/delete_all'")
    response = client.get("/admin/delete_all")

    logger.info("Post '/seed'")
    response = client.post("/seed", json=test_quotes_list)

    for quote in test_quotes_list['quotes']:
        logger.info("Get '/quote/name/" + quote['name'] + "'")
        response = client.get("/quote/name/" + quote['name'] )
        assert response.status_code == 200

        msg = response.json()
        del msg["backend"]
        logger.info(str(quote))
        logger.info("Quote Received " + str(msg["quotes"]))

        if msg["quotes"] != quote:
            assert False

def test_delete_quote_by_id():

    logger.info("Running '/quote/id/{id}' tests")

    logger.info("Get '/admin/delete_all'")
    response = client.get("/admin/delete_all")

    logger.info("Post '/seed'")
    response = client.post("/seed", json=test_quotes_list)

    logger.info("Get '/quotes/id'")
    response = client.get("/quotes/id")
    msg = response.json()

    quote_ids = []
    for quote in msg['quotes']:
        quote_ids.append(quote['id'])
    
    logger.debug("List of quote_ids", quote_ids=quote_ids)

    size_of_quotes = len(test_quotes_list['quotes'])
    for id in quote_ids:
        logger.info("Get '/quote/id/" + str(id) + "'")
        response = client.get("/quote/id/" + str(id))
        assert response.status_code == 200

        msg = response.json()
        del msg["backend"]
        logger.info("Quote Received " + str(msg["quotes"]))

        if msg["quotes"] not in test_quotes_list["quotes"]:
            assert False