from pydantic import BaseModel

class Canvas(BaseModel):
  email: str
  login: str
  password: str
  registration_date: str