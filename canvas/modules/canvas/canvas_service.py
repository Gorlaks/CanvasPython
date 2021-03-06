from fastapi.encoders import jsonable_encoder
from datetime import datetime

from canvas.modules.store.db import db
from canvas.models.canvas import CanvasTemplate, CanvasDataToCreate, CanvasTemplateToDelete
from canvas.models.response import ServerResponse
from canvas.modules.canvas.canvas_repository import canvas_repository
from canvas.utils.exceptions import ResponseException


class CanvasService:
    canvas_collection = None
    canvas_template_collection = None

    def __init__(self):
        self.canvas_collection = db["Canvas"]
        self.canvas_template_collection = db["CanvasTemplate"]

    def create_canvas(self, canvas_data: CanvasDataToCreate, user_id: str) -> str:
        canvas_template = canvas_repository.get_canvas_template(
            canvas_data.type)
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

    def create_canvas_template(self, canvasTemplateData: CanvasTemplate) -> ServerResponse:
        if not canvasTemplateData.type:
            raise ResponseException("Type is not set")
        if not canvasTemplateData.rows:
            raise ResponseException("Rows are not set")
        if not canvasTemplateData.columns:
            raise ResponseException("Columns are not set")
        if not canvasTemplateData.data:
            raise ResponseException("Data are not set")

        result = self.canvas_template_collection.insert_one({
            "ownerId": None,
            "title": None,
            "type": canvasTemplateData.type,
            "date": datetime.now(),
            "rows": canvasTemplateData.rows,
            "columns": canvasTemplateData.columns,
            "data": canvasTemplateData.data
        })
        return {
            "code": 0,
            "message": "Success"
        }

    def delete_canvas_template(self, data: CanvasTemplateToDelete) -> ServerResponse:
        try:
            canvas_id = data.canvas_id
            self.canvas_template_collection.delete_one({"canvasId": canvas_id})

            return {
                "code": 0,
                "message": "Success"
            }
        except Exception:
            raise ResponseException("Couldn't delete canvas template")


canvas_service = CanvasService()
