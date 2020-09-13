import pytest

from fastapi.testclient import TestClient
import sys
import os
import pathlib
import pytest
import importlib
import json


@pytest.mark.json
def test_json():

    json_file_path = str(pathlib.Path.cwd().joinpath("tests", "quotes", "quotes.json"))
    os.environ.update({"JSON_QUOTE_PATH": json_file_path})

    from crud.read_json import return_json_quotes
    from main import app

    quotes_list = return_json_quotes(json_file_path)

    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == 200

    msg = response.json()
    del msg["backend"]
    print(msg)

    if msg not in quotes_list["quotes"]:
        assert False


@pytest.mark.db
def test_db():

    json_file_path = str(pathlib.Path.cwd().joinpath("tests", "quotes", "initdb.sql"))
    os.environ["QUOTE_BACKEN"] = "DB"
    from main import app

    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == 200

    msg = response.json()
    del msg["backend"]
    print(msg)

    if msg not in quotes_list["quotes"]:
        assert False
