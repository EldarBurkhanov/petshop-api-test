import requests

class RequestHandler:

    BASE_URL = "https://petstore.swagger.io/v2"
    PET_URL = "pet"
    PET_FIND_BY_STATUS = "findByStatus"

    @staticmethod
    def post_pet(body):
        data = requests.post(f"{RequestHandler.BASE_URL}/{RequestHandler.PET_URL}", json=body)
        return data

    @staticmethod
    def put_pet(body):
        data = requests.put(f"{RequestHandler.BASE_URL}/{RequestHandler.PET_URL}", json=body)
        return data

    @staticmethod
    def find_pet_by_status(status):
        data = requests.get(f"{RequestHandler.BASE_URL}/{RequestHandler.PET_URL}/{RequestHandler.PET_FIND_BY_STATUS}",
                            params={"status": status})
        return data

    @staticmethod
    def get_pet_by_id(pet_id):
        data = requests.get(f"{RequestHandler.BASE_URL}/{RequestHandler.PET_URL}/{pet_id}")
        return data

    @staticmethod
    def update_pet_by_id(name, status):
        data = requests.post(f"{RequestHandler.BASE_URL}/{RequestHandler.PET_URL}/{id}",
                             data={"name": name, "status": status})
        return data

    @staticmethod
    def delete_pet_by_id(pet_id):
        data = requests.delete(f"{RequestHandler.BASE_URL}/{RequestHandler.PET_URL}/{pet_id}")
        return data


