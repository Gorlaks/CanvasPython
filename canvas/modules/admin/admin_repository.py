from typing import List

from canvas.models.user import User
from canvas.modules.store.db import db 


class AdminRepository:
    user_collection: List[User] = None

    def __init__(self):
        self.user_collection = db["User"]

    def get_users(self) -> List[User]:
        users = list(self.user_collection.find())
        for user in users:
            user["_id"] = str(user["_id"])
        return users

admin_repository = AdminRepository()