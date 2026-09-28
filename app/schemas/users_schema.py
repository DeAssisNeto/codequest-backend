import uuid
import datetime
from pydantic import BaseModel, EmailStr
from app.models.enums import UserRole


class UserBase(BaseModel):
    name: str
    birth_date: datetime.date
    gender: str
    email: EmailStr
    role: UserRole = UserRole.STUDENT


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: uuid.UUID
    active: bool

    model_config = {"from_attributes": True}
