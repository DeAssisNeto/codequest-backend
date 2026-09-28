import uuid
import datetime
from pydantic import BaseModel, EmailStr
from app.models.enums import UserRole


class UserBase(BaseModel):
    name: str
    birth_date: datetime.date
    gender: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: uuid.UUID
    role: UserRole
    active: bool

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    name: str | None = None
    birth_date: datetime.date | None = None
    gender: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    active: bool | None = None