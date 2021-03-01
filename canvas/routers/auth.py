from fastapi import APIRouter
from datetime import timedelta

from canvas.models.user import UserSignIn, UserSignUp
from canvas.models.response import ServerResponse
from canvas.modules.auth.auth_service import auth_service

from canvas.utils.jwt import create_access_token, get_current_user
from canvas.utils.jwt import ACCESS_TOKEN_EXPIRES_MINUTES

router = APIRouter()

@router.post("/login", response_model=ServerResponse)
def login(user_data: UserSignIn):
    authorized_user_data = auth_service.login(
        user_data.login, user_data.password)
    if (authorized_user_data["login"]):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
        access_token = create_access_token(
            data={"sub": authorized_user_data["login"]},
            expires_delta=access_token_expires
        )
    return { 
        "code": 0,
        "message": {
            "access_token": access_token
        }
    }


@router.post("/registration", response_model=ServerResponse)
def registration(user_data: UserSignUp):
    response = auth_service.registration(user_data)
    try:
        code = response.error_code
    except:
        code = 0
    return {
        "code": code,
        "message": {
            "Data": response
        }
    }