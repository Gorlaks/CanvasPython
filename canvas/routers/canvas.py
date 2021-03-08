from fastapi import APIRouter

from canvas.models.canvas import CanvasTemplateToCreate, CanvasDataToCreate, CanvasDataToUpdate
from canvas.utils.jwt import get_current_user
from canvas.modules.canvas.canvas_service import canvas_service
from canvas.modules.canvas.canvas_repository import canvas_repository
from canvas.models.response import ServerResponse
from canvas.utils.exceptions import ResponseException
from canvas.utils.helpers import check_for_admin

router = APIRouter()

@router.get("/get_canvas", response_model=ServerResponse)
def get_canvas(user_token: str, canvas_id: str):
    user = get_current_user(user_token)
    result = canvas_repository.get_canvas(user["id"], canvas_id)
    return result


@router.post("/create_canvas", response_model=ServerResponse)
def create_canvas(data: CanvasDataToCreate):
    '''
    Create a new empty Canvas table
    '''
    user = get_current_user(data.user_token)
    result = canvas_service.create_canvas(data, user["id"])
    return result


@router.delete("/delete_canvas", response_model=ServerResponse)
def delete_canvas(user_token: str, canvas_id: str):
    user = get_current_user(user_token)
    result = canvas_service.delete_canvas(user["id"], canvas_id)
    return result


@router.post("/update_canvas", response_model=ServerResponse)
def delete_canvas(data: CanvasDataToUpdate):
    user = get_current_user(data.user_token)
    result = canvas_service.update_canvas(data, user["id"])
    return result


@router.post("/create_canvas_template", response_model=ServerResponse)
def create_canvas_template(canvasTemplateData: CanvasTemplateToCreate):
    '''
    Create a new template of Canvas table
    '''
    user = check_for_admin(canvasTemplateData.user_token)

    result = canvas_service.create_canvas_template(canvasTemplateData)
    return result


@router.delete("/delete_canvas_template", response_model=ServerResponse)
def delete_canvas_template(user_token: str, canvas_type: str):
    user = check_for_admin(user_token)

    result = canvas_service.delete_canvas_template(canvas_type)
    return result


@router.get("/canvas_templates", response_model=ServerResponse)
def get_canvas_templates(user_token: str):
    user = check_for_admin(user_token)
    result = canvas_repository.get_canvas_templates()
    return {
        "code": 0,
        "message": {
            "data": result
        }
    }
