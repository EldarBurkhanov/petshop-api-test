import pytest
import allure
import requests


API_URL = "/pet/"


@allure.title("Test Delete pet")
@allure.description("This test sends a Delete request.")
@pytest.mark.parametrize("id, first_code, sec_code", [
    (0, 200, 404),
    (324, 200, 404),
])
def test_delete_pet(get_base_url, id, first_code, sec_code, ):

    # TODO Find some way to create a pet

    with allure.step(f"Send Delete request to delete pet"):
        data = requests.delete(get_base_url + API_URL + str(id))

    with allure.step("Check status code"):
        assert data.status_code == first_code

    with allure.step(f"Send Delete request to delete pet again"):
        data = requests.delete(get_base_url + API_URL + str(id))

    with allure.step("Check status code"):
        assert data.status_code == sec_code


@allure.title("Test Delete pet with invalid_id")
@allure.description("This test sends a Delete request with invalid id.")
def test_delete_invalid_id_pet(get_base_url):
    with allure.step(f"Send Delete request to unexciting pet"):
        data = requests.delete(get_base_url + API_URL + str("invalid_id"))

    with allure.step("Check status code"):
        assert data.status_code == 400
