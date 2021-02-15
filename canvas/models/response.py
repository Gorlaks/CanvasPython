from pydantic import BaseModel
from typing import Union

class ServerResponse(BaseModel):
  code: int
  message: Union[str, dict]