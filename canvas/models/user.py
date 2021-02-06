from pydantic import BaseModel

class UserData(BaseModel):
  login: str

class User(BaseModel):
  email: str
  login: str
  password: str
  registration_date: str