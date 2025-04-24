from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Any
from bson import ObjectId

from .user_role import UserRole

class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema: dict) -> None:
        field_schema.update(type="string")

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    role: UserRole

    class Config:
        json_encoders = {ObjectId: str}

class UserCreate(BaseModel):
    name: str
    password: str
    role: UserRole