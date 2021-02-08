from canvas.modules.store.db import db
from canvas.models.canvas import CanvasDataToCreate

class CanvasService:
    canvas_collection = None

    def __init__(self):
        self.canvas_collection = db["Canvas"]

    def create_canvas(self, data: CanvasDataToCreate, user_id: str) -> str:
        result = self.canvas_collection.insert_one({
            "title": data.title,
            "type": data.type,
            "ownerId": user_id,
            "date": "",
            "rows": 4,
            "columns": 5,
            "data": []
        })
        return str(result.inserted_id)

canvas_service = CanvasService()