from typing import Dict

from canvas.utils.jwt import get_current_user
from canvas.utils.exceptions import ResponseException


def destruct_dict(data: Dict[str, str]) -> str:
    return list(map(lambda x: x[1], sorted(data)))


def check_for_admin(access_token: str):
    user = get_current_user(access_token)

    if (user["login"] != "admin"):
        raise ResponseException(
            "You have to be an admin to create a new canvas template")
