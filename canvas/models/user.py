from pydantic import BaseModel

class UserData(BaseModel):
  login: str