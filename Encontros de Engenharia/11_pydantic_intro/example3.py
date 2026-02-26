# AFTER, BEFORE, WRAP, PLAIN
from typing import Annotated, Any
from pydantic import ValidationError, AfterValidator, BeforeValidator, PlainValidator, WrapValidator, ValidatorFunctionWrapHandler, BaseModel

def is_valid_password(value: str):
    if not len(value) >= 8:
        raise ValueError("Senha precisa de 8 caracteres")
    return value

class UserModel(BaseModel):
    user: str
    password: Annotated[str, AfterValidator(is_valid_password)]

class UserModelBefore(BaseModel):
    user: str
    password: Annotated[str, BeforeValidator(is_valid_password)]

def is_valid_password(value: Any):
    if isinstance(value, str):
        return value
    elif isinstance(value, int):
        return value * 2
    else:
        return "string invalida"

class UserModelPlain(BaseModel):
    password: Annotated[str, PlainValidator(is_valid_password)]


def is_valid_password(value: Any, handler: ValidatorFunctionWrapHandler):
    try:
        if isinstance(value, list):
            raise
        handler(value)
    except ValidationError as err:
        if err.errors()[0]["type"] == "string_type":
            return handler(str(value))
        else:
            raise

class UserWrapModel(BaseModel):
    password: Annotated[str, WrapValidator(is_valid_password)]

