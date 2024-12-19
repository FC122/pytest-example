import pytest
import json
import os
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def config()->dict:
    with open(f'config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

@pytest.fixture(scope="session")
def requests(playwright: Playwright) -> APIRequestContext:
    return playwright.request.new_context()