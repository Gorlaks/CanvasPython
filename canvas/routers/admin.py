from fastapi import APIRouter
from typing import List

from canvas.modules.admin.admin_repository import admin_repository
from canvas.models.user import User
from canvas.utils.jwt import get_current_user
from canvas.models.response import ServerResponse

router = APIRouter()


@router.post("/admin/get_users", response_model=ServerResponse)
def get_users(access_token: str):
    user = get_current_user(access_token)
    if user["login"] == "admin":
        return {
            "code": 0,
            "message": {
                "users": admin_repository.get_users()
            }
        }
    else:
        return {
            "code": 1,
            "message": "You have no permissions"
        }
