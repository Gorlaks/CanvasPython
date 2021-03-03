from pydantic import BaseModel
from typing import List, Dict, Optional

class Canvas(BaseModel):
  ownerId: str
  title: str
  type: str
  date: str
  rows: int
  columns: int
  data: List[Dict]

class CanvasTemplate(Canvas):
  user_token: str
  ownerId: Optional[str] = None
  title: Optional[str] = None

class CanvasDataToCreate(BaseModel):
  user_token: str
  title: str
  type: str