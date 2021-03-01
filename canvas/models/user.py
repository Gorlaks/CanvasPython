from typing import Optional
from pydantic import BaseModel
from fastapi import Query


class User(BaseModel):
    email: str
    login: str


class UserSignIn(User):
    email: Optional[str] = None
    password: str


class UserSignUp(UserSignIn):
    password: str = Query(None, min_length=6)


class UserTokenData(BaseModel):
    login: str
