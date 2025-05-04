from bson import ObjectId
from pydantic import BaseModel

from .user_role import UserRole


class User(BaseModel):
    name: str
    role: UserRole

    class Config:
        json_encoders = {ObjectId: str}

class UserCreate(BaseModel):
    name: str
    password: str
    role: UserRole

class UserLogin(BaseModel):
    name: str
    password: str