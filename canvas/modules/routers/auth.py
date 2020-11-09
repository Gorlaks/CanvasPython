from fastapi import APIRouter

from canvas.models.auth import User
from canvas.models.response import Response
from canvas.modules.auth.auth_service import AuthService

router = APIRouter()

auth_service = AuthService()

@router.post("/login")
def login(user_data: User) -> Response:
  return auth_service.login(user_data.login, user_data.password)

@router.post("/registration")
def registration(user_data: User) -> Response:
  return auth_service.registration(user_data)