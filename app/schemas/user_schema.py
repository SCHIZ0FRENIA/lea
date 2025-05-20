from bson import ObjectId
from pydantic import BaseModel

from .user_role import UserRole


class User(BaseModel):
    login: str
    role: UserRole

    class Config:
        json_encoders = {ObjectId: str}

class UserCreate(BaseModel):
    login: str
    password: str
    role: UserRole

class UserLogin(BaseModel):
    login: str
    password: str