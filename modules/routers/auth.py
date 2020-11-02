from fastapi import APIRouter

from ..auth.auth_repository import AuthRepository

router = APIRouter()

@router.get("/login")
def login():
  auth_repository = AuthRepository()
  return auth_repository.get_user_data()