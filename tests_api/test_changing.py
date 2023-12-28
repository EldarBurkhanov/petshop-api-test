import pytest
import allure
import requests
from model_validator import ResponceBody


API_URL = "/pet"


@pytest.mark.parametrize("status, status_code, name, id", [
    ("sold", 200, "Korjik", 1),
    ("lost", 405, "Manny", 1),
    ("sold", 400, "Timi", "incorrect_id"),

])
def test_change_pet(get_base_url, get_default_body, status, status_code, id, name):

    data = requests.post(get_base_url + API_URL + f"/{id}", data={"name": name, "status": status})

    assert data.status_code == status_code

    assert ResponceBody(**data.json())



