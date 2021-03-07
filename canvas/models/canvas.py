from pydantic import BaseModel
from typing import List, Dict, Optional


class Canvas(BaseModel):
    owner_id: str
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


class CanvasTemplateToCreate(Canvas):
    user_token: str
    owner_id: Optional[str] = None
    title: Optional[str] = None


class CanvasTemplate(Canvas):
    owner_id: Optional[str] = None
    title: Optional[str] = None


class CanvasTemplateToDelete(BaseModel):
    user_token: str
    canvas_type: str
