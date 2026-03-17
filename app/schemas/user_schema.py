from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str
    password: str


class UserLogin(BaseModel):
    phone: str
    password: str