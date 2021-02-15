from fastapi import APIRouter
from typing import List

from canvas.modules.user.user_repository import user_repository

from canvas.models.canvas import Canvas

from canvas.utils.jwt import get_current_user

router = APIRouter()

@router.post("/get_user_canvases", response_model=List[Canvas])
def get_user_canvases(user_token: str):
  user = get_current_user(user_token)
  return user_repository.get_user_canvases(user["login"])