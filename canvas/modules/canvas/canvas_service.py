from canvas.modules.store.db import db
from canvas.models.canvas import Canvas, CanvasDataToCreate
from canvas.models.response import ServerResponse

class CanvasService:
    canvas_collection = None
    canvas_template_collection = None

    def __init__(self):
        self.canvas_collection = db["Canvas"]
        self.canvas_template_collection = db["CanvasTemplate"]

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

    def create_canvas_template(self, canvasTemplateData: Canvas) -> ServerResponse:
        result = self.canvas_template_collection.insert_one(canvasTemplateData.dict())
        return {
            "code": 0,
            "message": "Success"
        }

canvas_service = CanvasService()