import os


OUT_DIR="test_out"


def pytest_sessionstart(session):

    if not os.path.isdir(OUT_DIR):
        os.mkdir(OUT_DIR)
