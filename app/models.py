from pydantic import BaseModel


class User(BaseModel):
    name: str
    middle_name: str
    district: str
    city: str


class Action(BaseModel):
    name: str
    company: str
    street: str
    number: str
    district: str
    city: str
    description: str
