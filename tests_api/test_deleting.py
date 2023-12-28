import pytest
import allure
import requests
from model_validator import ResponceBody


API_URL = "/pet/"

@pytest.mark.parametrize("id, first_code, sec_code", [
    (0, 200, 404),
    (324, 200, 404),
])
def test_delete_pet(get_base_url, id, first_code, sec_code, ):

    #TODO Find some way to create a pet

    data = requests.delete(get_base_url + API_URL + str(id))

    assert data.status_code == first_code

    data = requests.delete(get_base_url + API_URL + str(id))

    assert data.status_code == sec_code


def test_delete_invalid_id_pet(get_base_url):
    data = requests.delete(get_base_url + API_URL + str("invalid_id"))

    assert data.status_code == 400
