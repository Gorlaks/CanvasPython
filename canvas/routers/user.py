from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

from canvas.modules.user.user_repository import user_repository
from canvas.models.response import ServerResponse

from canvas.models.canvas import Canvas

from canvas.utils.jwt import get_current_user

router = APIRouter()

class UserCanvasesRequestData(BaseModel):
  access_token: str

@router.post("/get_user_canvases", response_model=ServerResponse)
def get_user_canvases(data: UserCanvasesRequestData):
  '''
  Get all Canvases owned by some user
  '''
  user = get_current_user(data.access_token)
  canvases = user_repository.get_user_canvases(user["id"])
  return {
    "code": 0,
    "message": {
      "canvases": canvases
    }
  }