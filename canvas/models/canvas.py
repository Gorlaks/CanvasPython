from pydantic import BaseModel
from typing import List, Dict

class Canvas(BaseModel):
  ownerId: str
  title: str
  type: str
  date: str
  rows: int
  columns: int
  data: List[Dict]

class CanvasDataToCreate(BaseModel):
  user_token: str
  title: str
  type: str