from dataclasses import dataclass
from pydantic import BaseModel, field_validator


class User:
    def __init__(self, email: str):
        self.email = email
    
    def see_email(self):
        return self.email

@dataclass
class UserDataclass:
    name: str
    email: str
    password: str

class UserModel(BaseModel):
    name: str
    email: str
    password: str

    @field_validator("email")
    def check_email(cls, value):
        if "@" not in value:
            raise ValueError("Não é um email válido!")
        return value

class UserOutput(UserModel):
    user_id: int