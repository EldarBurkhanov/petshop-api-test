from pydantic import BaseModel, field_validator, ValidationError
from typing import List


class Category(BaseModel):
    id: int
    name: str


class Tags(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tags]
    status: str

    @field_validator("status")
    def validate_color(cls, value):
        if value not in ["sold", "available", "pending"]:
            raise ValueError(f"Invalid status format {value}, should be sold/available/pending")
        return value


class PetList(BaseModel):
    pet_list_data: List[Pet]


class ResponseBody(BaseModel):
    code: int
    type: str
    message: str
