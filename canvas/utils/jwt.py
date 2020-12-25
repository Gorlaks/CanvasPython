from datetime import timedelta, datetime
from jose import JWTError, jwt
from typing import Optional

SECRET_KEY = "c603f8eb5cf8796accced19850d80ca93cb397b39e29e73e7d4df581022ea709"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRES_MINUTES)
  
  to_encode.update({ "exp": expire })
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
  return encoded_jwt