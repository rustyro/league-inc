import os

import pytest
from flask import Flask


@pytest.fixture(scope="session")
def app():
    from app import app
    from app import view
    yield app


@pytest.fixture()
def get_file():
    def find_file(filepath):
        filename = filepath.split("/")[-1]
        files = (open(filepath, 'rb'), filename)
        return files
    return find_file
