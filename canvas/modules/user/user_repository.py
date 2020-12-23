from typing import List

from canvas.modules.store.db import db
from canvas.models.canvas import Canvas

class UserRepository:
  canvas_collection: List[Canvas] = None

  def __init__(self):
    self.canvas_collection = db["canvas"]

  def get_users_canvases_list(self):
    return []