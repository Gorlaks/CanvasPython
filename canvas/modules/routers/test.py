from fastapi import APIRouter
from datetime import timedelta

from ...utils.jwt import create_access_token
from ...utils.jwt import ACCESS_TOKEN_EXPIRES_MINUTES

router = APIRouter()


@router.post("/test_creating_jwt")
def test_creating_jwt(username):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = create_access_token(data={"sub": username},
                                       expires_delta=access_token_expires)
    if (access_token):
        return {"access_token": access_token}
    else:
        return {"access_token": "Fail"}
