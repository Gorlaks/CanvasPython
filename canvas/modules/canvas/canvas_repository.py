from typing import List
from bson.objectid import ObjectId

from canvas.modules.store.db import db
from canvas.models.canvas import Canvas, CanvasTemplate
from canvas.models.response import ServerResponse
from canvas.utils.exceptions import ResponseException


class CanvasRepository:
    canvas_collection: List[Canvas]
    canvas_template_collection: List[Canvas]

    def __init__(self):
        self.canvas_collection = db["Canvas"]
        self.canvas_template_collection = db["CanvasTemplate"]

    def get_canvas(self, user_id: str, canvas_id: str) -> ServerResponse:
        try:
            result = self.canvas_collection.find_one(
                {"ownerId": user_id, "_id": ObjectId(canvas_id)})
            result["_id"] = str(result["_id"])
            return {
                "code": 0,
                "message": {
                    "data": result
                }
            }
        except Exception:
            raise ResponseException("Couldn't get canvas")

    def get_canvas_template(self, canvas_type: str) -> Canvas:
        result: Canvas = self.canvas_template_collection.find_one(
            {"type": canvas_type})
        return result

    def get_canvas_templates(self) -> List[CanvasTemplate]:
        templates: List[CanvasTemplate] = list(
            self.canvas_template_collection.find())
        for template in templates:
            template["_id"] = str(template["_id"])
        return templates


canvas_repository = CanvasRepository()
