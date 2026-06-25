from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    degree: Optional[str] = None
    skills: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    degree: Optional[str] = None
    skills: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str