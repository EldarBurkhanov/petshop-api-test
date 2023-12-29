import pytest
import allure
import requests
from model_validator import Pet

API_URL = "/pet"

@allure.title("Test Create pet via POST Request")
@allure.description("This test sends a POST request to createe a pet and check response body.")
@pytest.mark.parametrize(
    "id, category, name, photoUrls, tags, status, status_code",
    [(
                  22,
                  {"id": 2, "name": "Torpeda"},
                  "Korjik",
                  ["https://somethin.jpg, https://anything.jpg"],
                  [{"id": 1, "name": "serj"}],
                  "available",
                  200),

    pytest.param(30,
                  {"id":123, "name":"Sunny"},
                  "Lexa",
                  ["https://sometsdhin.jpg, https://ankkking.jpg"],
                  [{"id": 12, "name": "sanya"}],
                  "pending",
                  200,
                  marks=pytest.mark.xfail(reason="My Fail")),

    pytest.param(8,
                 {"id": 12, "name": "Torpeda"},
                 "Mark",
                 ["https://somethin.jpg, https://anything.jpg"],
                 [{"id": 33, "name": "dima"}],
                 "sold",
                 888,
                 marks=pytest.mark.skip(reason="My SKip")),
])
def test_create_pet(get_base_url: str,
                    get_default_body: dict,
                    id: int,
                    category: dict,
                    name: str,
                    photoUrls: list,
                    tags: list,
                    status: str,
                    status_code: int,
                    ):

    body = dict(get_default_body)
    body["id"] = id
    body["category"] = category
    body["name"] = name
    body["photoUrls"] = photoUrls
    body["tags"] = tags
    body["status"] = status

    with allure.step("Send POST to create pet"):
        data = requests.post(get_base_url + API_URL, json=body)

    with allure.step("Check status code"):
        assert data.status_code == status_code

    with allure.step("Validate response data"):
        assert Pet(**data.json())

    pet = Pet(**data.json())

    with allure.step("Check pet id"):
        assert pet.id == id

    with allure.step("Check pet category id"):
        assert pet.category.id == category["id"]

    with allure.step("Check pet category name"):
        assert pet.category.name == category["name"]

    with allure.step("Check pet name"):
        assert pet.name == name

    with allure.step("Check PhotoUrls"):
        assert pet.photoUrls == photoUrls

    with allure.step("Check Tag Name"):
        assert pet.tags[0].name == tags[0]["name"]

    with allure.step("Check Tag Id"):
        assert pet.tags[0].id == tags[0]["id"]

    with allure.step("Check Status"):
        assert pet.status == status


@allure.title("Test Create pet with empty DICT")
@allure.description("This test sends a POST request with empty Dictionary.")
def test_empty_dict(get_base_url):
    body = {}

    with allure.step("Send POST to create pet with empty dict"):
        data = requests.post(get_base_url + API_URL, json=body)

    with allure.step("Check status code"):
        assert data.status_code == 405


@allure.title("Test Create pet without DICT")
@allure.description("This test sends a POST request without Dictionary.")
def test_no_dict(get_base_url):

    with allure.step("Send POST to create pet without dict"):
        data = requests.post(get_base_url + API_URL)

    with allure.step("Check status code"):
        assert data.status_code == 415

