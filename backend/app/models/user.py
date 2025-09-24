from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
