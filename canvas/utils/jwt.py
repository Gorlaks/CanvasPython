from datetime import timedelta, datetime
from jose import JWTError, jwt
from jose import JWTError
from typing import Optional
from fastapi import HTTPException, status

from canvas.models.jwt import TokenData
from canvas.models.user import UserTokenData
from canvas.modules.auth.auth_repository import auth_repository

SECRET_KEY = "c603f8eb5cf8796accced19850d80ca93cb397b39e29e73e7d4df581022ea709"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 240

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRES_MINUTES)
  
  to_encode.update({ "exp": expire })
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
  return encoded_jwt

def get_current_user(token: str) -> UserTokenData:
  credentials_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Couldn't validate credentials",
    headers = {"WWW-Authenticate": "Bearer"}
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
      raise credentials_exception
    token_data = TokenData(username=username)
  except JWTError:
    raise credentials_exception
  data = auth_repository.get_user_data(username)
  if data["login"] is None:
    raise credentials_exception
  return { "id": str(data["_id"]), "login": username }