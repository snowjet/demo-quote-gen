import pytest


def pytest_addoption(parser):
    parser.addoption("--db", action="store_true", default=False, help="run DB test")


def pytest_configure(config):
    config.addinivalue_line("markers", "db: Run Database tests")
    config.addinivalue_line("markers", "json: Run JSON tests")


def pytest_collection_modifyitems(config, items):

    if config.getoption("--db"):
        skip_msg = "run DB tests"
        skip_test = "json"
    else:
        skip_msg = "run json tests"
        skip_test = "db"

    skip_mark = pytest.mark.skip(reason=skip_msg)

    for item in items:
        if skip_test in item.keywords:
            item.add_marker(skip_mark)
