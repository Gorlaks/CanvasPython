from pydantic import BaseModel
from typing import List, Dict, Optional


class Canvas(BaseModel):
    owner_id: str
    title: str
    type: str
    rows: int
    columns: int
    data: List[Dict]


class CanvasDataToUpdate(BaseModel):
    access_token: str
    canvas_id: str
    title: str
    data: List[Dict]
    

class CanvasDataToCreate(BaseModel):
    access_token: str
    title: str
    type: str


class CanvasTemplateToCreate(Canvas):
    access_token: str
    owner_id: Optional[str] = None
    title: Optional[str] = None


class CanvasTemplate(Canvas):
    owner_id: Optional[str] = None
    title: Optional[str] = None
