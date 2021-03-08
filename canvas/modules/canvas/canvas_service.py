from fastapi.encoders import jsonable_encoder
from datetime import datetime
from bson.objectid import ObjectId

from canvas.modules.store.db import db
from canvas.models.canvas import CanvasTemplateToCreate, CanvasDataToCreate, CanvasDataToUpdate
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

    def delete_canvas(self, user_id: str, canvas_id: str) -> ServerResponse:
        try:
            result = self.canvas_collection.delete_one(
                {"ownerId": user_id, "_id": ObjectId(canvas_id)})
            return {
                "code": 0,
                "message": "Success"
            }
        except Exception:
            raise ResponseException(Exception)

    def update_canvas(self, data: CanvasDataToUpdate, user_id: str) -> ServerResponse:
        try:
            result = self.canvas_collection.update_one(
                {"ownerId": user_id, "_id": ObjectId(data.canvas_id)},
                {"$set": {"title": data.title, "data": data.data}}
            )
            return {
                "code": 0,
                "message": "Success"
            }
        except Exception:
            raise ResponseException(Exception)

    def create_canvas_template(self, canvasTemplateData: CanvasTemplateToCreate) -> ServerResponse:
        canvas_type = canvasTemplateData.type
        if not canvas_type:
            raise ResponseException("Type is not set")
        if not canvasTemplateData.rows:
            raise ResponseException("Rows are not set")
        if not canvasTemplateData.columns:
            raise ResponseException("Columns are not set")
        if not canvasTemplateData.data:
            raise ResponseException("Data are not set")

        isExist = self.canvas_template_collection.find_one(
            {"type": canvas_type}) != None

        if (isExist):
            raise ResponseException("Such Canvas type is already exist")

        result = self.canvas_template_collection.insert_one({
            "ownerId": None,
            "title": None,
            "type": canvas_type,
            "date": datetime.now(),
            "rows": canvasTemplateData.rows,
            "columns": canvasTemplateData.columns,
            "data": canvasTemplateData.data
        })
        return {
            "code": 0,
            "message": "Success"
        }

    def delete_canvas_template(self, canvas_type: str) -> ServerResponse:
        try:
            self.canvas_template_collection.delete_one({"type": canvas_type})
            return {
                "code": 0,
                "message": "Success"
            }
        except Exception:
            raise ResponseException("Couldn't delete canvas template")


canvas_service = CanvasService()
