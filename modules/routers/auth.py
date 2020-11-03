from fastapi import APIRouter

from models.auth import User
from ..auth.auth_service import AuthService

router = APIRouter()

@router.post("/login")
def login(user_data: User):
  auth_service = AuthService()
  return auth_service.login(user_data.login)