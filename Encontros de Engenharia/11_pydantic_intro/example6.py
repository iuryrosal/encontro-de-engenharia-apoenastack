from pydantic_settings import BaseSettings
from pydantic import Field

from dotenv import load_dotenv

class DevEnvConfig(BaseSettings):
    env: str = Field(alias="env")

class ProdEnvConfig(BaseSettings):
    env: str = Field(alias="env")
    api_key: str
    

load_dotenv()
print(DevEnvConfig().model_dump())