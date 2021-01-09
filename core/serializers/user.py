from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    district: str
    city: str


class UpdateUser(BaseModel):
    district: str
    city: str