from canvas.modules.store.db import db
from canvas.models.canvas import CanvasDataToCreate

class CanvasService:
    canvas_collection = None

    def __init__(self):
        self.canvas_collection = db["Canvas"]

    def create_canvas(self, data, user_id: str):
        data["user_token"] = None
        data["ownerId"] = user_id
        data["date"] = ""
        data["rows"] = 4
        data["columns"] = 5
        data["data"] = []
        self.canvas_collection.insert_one(data)
        return data

canvas_service = CanvasService()