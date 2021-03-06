from typing import List

from canvas.modules.store.db import db
from canvas.models.canvas import Canvas, CanvasTemplate

class CanvasRepository:
  canvas_template_collection: List[Canvas]

  def __init__(self):
    self.canvas_template_collection = db["CanvasTemplate"]

  def get_canvas_template(self, canvas_type: str) -> Canvas:
    result: Canvas = self.canvas_template_collection.find_one({ "type": canvas_type })
    return result

  def get_canvas_templates(self) -> List[CanvasTemplate]:
    templates: List[CanvasTemplate] = list(self.canvas_template_collection.find())
    for template in templates:
      template["_id"] = str(template["_id"])
    return templates

canvas_repository = CanvasRepository()