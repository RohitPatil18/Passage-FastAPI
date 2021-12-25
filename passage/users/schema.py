from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str 
    last_name: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserRead(UserBase):
    id: Optional[int]
    email: EmailStr
    is_active: bool

class UserUpdate(UserBase):
    pass