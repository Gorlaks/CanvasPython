from typing import List

from canvas.modules.store.db import db
from canvas.models.canvas import Canvas
from canvas.models.user import User


class UserRepository:
    canvas_collection: List[Canvas] = None

    def __init__(self):
        self.canvas_collection = db["Canvas"]

    def get_user_canvases(self, login):
        canvases = self.canvas_collection.find_one({"login": login})
        return canvases

user_repository = UserRepository()