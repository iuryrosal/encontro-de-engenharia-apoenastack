from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class UserDetails(BaseModel):
    address: str
    phone: str

class UserInput(BaseModel):
    username: str
    password: Optional[str] = None
    details: UserDetails

class UserOutput(UserInput):
    env: str = "Name"

app = FastAPI()

@app.post("/user")
def get_user(user_data: UserInput) -> UserOutput:
    return UserOutput(**user_data.model_dump())