import pytest
import allure
import requests
from model_validator import PetList

API_URL = "pet/findByStatus"


@allure.title("Test Searching pet by status")
@allure.description("This test sends a get request for search pets by theris status.")
@pytest.mark.parametrize("status, status_code", [
    ("sold", 200),
    ("pending", 200),
    ("available", 200),
    ("lost", 400),
])
def test_search_by_status(get_base_url, status, status_code):
    with allure.step(f"Send Delete request to delete pet"):
        data = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params={"status": status})

    with allure.step(f"Check status code"):
        assert data.status_code == status_code

    a = {"pet_list_data": data.json()}

    with allure.step(f"Validate response by PetList model"):
        assert PetList(**a)

    #TODO Add check for valid status (Sometging went wrong)

