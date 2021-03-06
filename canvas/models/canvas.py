from pydantic import BaseModel
from typing import List, Dict, Optional


class Canvas(BaseModel):
    owner_id: str
    title: str
    type: str
    rows: int
    columns: int
    data: List[Dict]


class CanvasDataToSend(BaseModel):
    title: str
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


class CanvasTemplateToCreate(BaseModel):
    access_token: str
    type: str
    rows: int
    columns: int
    data: List[Dict]


class CanvasTemplate(Canvas):
    owner_id: Optional[str] = None
    title: Optional[str] = None