from fastapi import APIRouter
from typing import List

from canvas.modules.user.user_repository import UserRepository 

from canvas.models.user import UserData
from canvas.models.canvas import Canvas

router = APIRouter()

userRepository = UserRepository()

@router.post("/users_canvases_list")
def get_users_canvases_list(used_data: UserData) -> List[Canvas]:
  return ["Hello", "World", "!"]