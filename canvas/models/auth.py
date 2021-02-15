from typing import Optional
from pydantic import BaseModel
from fastapi import Query

class UserBase(BaseModel):
  email: str
  login: str
  password: str

class UserSignIn(UserBase):
  email: Optional[str] = None

class User(UserSignIn):
  pass

class UserSignUp(UserSignIn):
  password: str = Query(None, min_length=6)