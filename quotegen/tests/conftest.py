import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--postgresql",
        action="store_true",
        default=False,
        help="Run postgresql database tests",
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "postgresql: Run postgresql database tests")
    config.addinivalue_line("markers", "mysql: Run postgresql database tests")
    config.addinivalue_line("markers", "sqlite: Run sqlite database tests")


def pytest_collection_modifyitems(config, items):

    if config.getoption("--postgresql"):
        skip_msg = "run DB tests"
        skip_test = "sqlite"
    else:
        skip_msg = "run json tests"
        skip_test = "postgresql"

    skip_mark = pytest.mark.skip(reason=skip_msg)

    for item in items:
        if skip_test in item.keywords:
            item.add_marker(skip_mark)
