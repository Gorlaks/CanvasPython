from fastapi.encoders import jsonable_encoder
from datetime import datetime

from canvas.modules.store.db import db
from canvas.models.canvas import Canvas, CanvasDataToCreate
from canvas.models.response import ServerResponse
from canvas.modules.canvas.canvas_repository import canvas_repository

class CanvasService:
    canvas_collection = None
    canvas_template_collection = None

    def __init__(self):
        self.canvas_collection = db["Canvas"]
        self.canvas_template_collection = db["CanvasTemplate"]

    def create_canvas(self, canvas_data: CanvasDataToCreate, user_id: str) -> str:
        canvas_template = canvas_repository.get_canvas_template(canvas_data.type)
        result = self.canvas_collection.insert_one({
            "ownerId": user_id,
            "title": canvas_data.title,
            "type": canvas_data.type,
            "date": datetime.now(),
            "rows": canvas_template["rows"],
            "columns": canvas_template["columns"],
            "data": canvas_template["data"]
        })
        return {
            "code": 0,
            "message": {
                "created_canvas_id": str(result.inserted_id)
            }
        }
        


    def create_canvas_template(self, canvasTemplateData: Canvas) -> ServerResponse:
        result = self.canvas_template_collection.insert_one(canvasTemplateData.dict())
        return {
            "code": 0,
            "message": "Success"
        }

canvas_service = CanvasService()