import pytest
import allure
import requests
from model_validator import ResponceBody


API_URL = "/pet"


@allure.title("Test Update pet info  via POST Request")
@allure.description("This test sends a POST request to update pet data.")
@pytest.mark.parametrize("status, status_code, name, id", [
    ("sold", 200, "Korjik", 1),
    ("lost", 405, "Manny", 1),
    ("sold", 400, "Timi", "incorrect_id"),

])
def test_change_pet(get_base_url, get_default_body, status, status_code, id, name):

    with allure.step(f"Send POST request to update pet: {status}, {status_code}, {id}, {name}"):
        data = requests.post(get_base_url + API_URL + f"/{id}", data={"name": name, "status": status})

    with allure.step(f"Verify the response status code is {status_code}"):
        assert data.status_code == status_code

    with allure.step("Validate the response data against the ResponceBody model"):
        assert ResponceBody(**data.json())



