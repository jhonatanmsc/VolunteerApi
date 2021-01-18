from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    district: str
    city: str
    disabled: Optional[bool] = True


# mandar numero conta da vo para josimar
class AuthUser(User):
    password: str
    password2: str


class UserCredentials(BaseModel):
    email: str
    password: str


class UpdateUser(BaseModel):
    district: str
    city: str
