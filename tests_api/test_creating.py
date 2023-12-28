import pytest
import allure
import requests
from model_validator import Pet

API_URL = "/pet"


@pytest.mark.parametrize(
    "id, category, name, photoUrls, tags, status, status_code",
    [(
                  22,
                  {"id":2, "name":"Torpeda"},
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

    data = requests.post(get_base_url + API_URL, json=body)

    assert data.status_code == status_code

    assert Pet(**data.json())

    pet = Pet(**data.json())

    assert pet.id == id

    assert pet.category.id == category["id"]

    assert pet.category.name == category["name"]

    assert pet.name == name

    assert pet.photoUrls == photoUrls

    assert pet.tags[0].name == tags[0]["name"]

    assert pet.tags[0].id == tags[0]["id"]

    assert pet.status == status


def test_empty_dict(get_base_url):
    body = {}

    data = requests.post(get_base_url + API_URL, json=body)

    assert data.status_code == 405


def test_no_dict(get_base_url):

    data = requests.post(get_base_url + API_URL)

    assert data.status_code == 415

