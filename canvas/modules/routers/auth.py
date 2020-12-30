from fastapi import APIRouter
from datetime import timedelta

from canvas.models.auth import User
from canvas.models.response import Response
from canvas.modules.auth.auth_service import AuthService

from ...utils.jwt import create_access_token
from ...utils.jwt import ACCESS_TOKEN_EXPIRES_MINUTES

router = APIRouter()

auth_service = AuthService()


@router.post("/login")
def login(user_data: User) -> Response:
    authorized_user_data = auth_service.login(
        user_data.login, user_data.password)
    if (authorized_user_data["login"]):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
        access_token = create_access_token(
            data={"sub": authorized_user_data["login"]},
            expires_delta=access_token_expires
        )
    return {"access_token": access_token}


@router.post("/registration")
def registration(user_data: User) -> Response:
    return auth_service.registration(user_data)
