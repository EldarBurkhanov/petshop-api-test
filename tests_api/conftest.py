import pytest
import allure

BASE_URL = "https://petstore.swagger.io/v2"

DEFAULT_BODY = {
            "id": 1,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "Korjik",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
           }

"""Hook for add custom marks"""
def pytest_configure(config):
    config.addinivalue_line("markers", "delete_method: mark a test as a DELETE method test")

@pytest.fixture
def get_base_url():
    return BASE_URL


@pytest.fixture
def get_default_body():
    return DEFAULT_BODY
