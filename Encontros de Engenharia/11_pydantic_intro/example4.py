from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

class UserPayload(BaseModel):
    user_id: int
    email: EmailStr
    name: Annotated[str, Field(..., min_length=5)]
    address: str
    phone: str