from fastapi import APIRouter

from canvas.models.canvas import CanvasTemplate, CanvasDataToCreate, CanvasTemplateToDelete
from canvas.utils.jwt import get_current_user
from canvas.modules.canvas.canvas_service import canvas_service
from canvas.models.response import ServerResponse
from canvas.utils.exceptions import ResponseException

router = APIRouter()


@router.post("/create_canvas", response_model=ServerResponse)
def create_canvas(data: CanvasDataToCreate):
    '''
    Create a new empty Canvas table
    '''
    user = get_current_user(data.user_token)
    result = canvas_service.create_canvas(data, user["id"])
    return result


@router.post("/create_canvas_template", response_model=ServerResponse)
def create_canvas_template(canvasTemplateData: CanvasTemplate):
    '''
    Create a new template of Canvas table
    '''
    user = get_current_user(canvasTemplateData.user_token)

    if (user["login"] != "admin"):
        raise ResponseException(
            "You have to be an admin to create a new canvas template")

    result = canvas_service.create_canvas_template(canvasTemplateData)
    return result


@router.post("/delete_canvas_template", response_model=ServerResponse)
def delete_canvas_template(data: CanvasTemplateToDelete):
    user = get_current_user(data.user_token)
    
    if (user["login"] != "admin"):
        raise ResponseException(
            "You have to be an admin to create a new canvas template")

    result = canvas_service.delete_canvas_template(data)
    return result