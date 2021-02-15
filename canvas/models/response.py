from pydantic import BaseModel

class ServerResponse(BaseModel):
  code: int
  message: str or dict