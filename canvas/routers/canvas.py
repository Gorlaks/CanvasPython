from fastapi import APIRouter

from canvas.models.canvas import CanvasDataToCreate
from canvas.utils.jwt import get_current_user
from canvas.modules.canvas.canvas_service import canvas_service
from canvas.models.response import Response

router = APIRouter()


@router.post("/create_canvas")
def create_canvas(data: CanvasDataToCreate) -> Response:
    user = get_current_user(data.user_token)
    result = canvas_service.create_canvas(data, user["id"])
    return {
        "code": 0,
        "message": result
    }
