from typing import List

from canvas.modules.store.db import db
from canvas.models.canvas import Canvas

class CanvasRepository:
  canvas_template_collection: List[Canvas]

  def __init__(self):
    self.canvas_template_collection = db["CanvasTemplate"]

  def get_canvas_template(self, canvas_type: str) -> Canvas:
    result = self.canvas_template_collection.find_one({ "type": canvas_type })
    return result

canvas_repository = CanvasRepository()