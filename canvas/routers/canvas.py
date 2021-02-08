from fastapi import APIRouter
import json

from canvas.models.canvas import CanvasDataToCreate
from canvas.utils.jwt import get_current_user
from canvas.modules.canvas.canvas_service import canvas_service

router = APIRouter()


@router.post("/create_canvas")
def create_canvas(data):
    data = json.loads(data)
    user = get_current_user(data["user_token"])
    # canvas_service.create_canvas(data, user["id"])
    return user
