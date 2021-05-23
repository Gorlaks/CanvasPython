from fastapi import APIRouter

from canvas.models.canvas import CanvasTemplateToCreate, CanvasDataToCreate, CanvasDataToUpdate, CanvasDataToSend
from canvas.utils.jwt import get_current_user
from canvas.modules.canvas.canvas_service import canvas_service
from canvas.modules.canvas.canvas_repository import canvas_repository
from canvas.models.response import ServerResponse
from canvas.utils.exceptions import ResponseException
from canvas.utils.helpers import check_for_admin

from canvas.modules.spam_detection.mail import send_mail
from canvas.modules.spam_detection.spam_detection import check_data_for_spam

router = APIRouter()

@router.get("/get_canvas", response_model=ServerResponse)
def get_canvas(access_token: str, canvas_id: str):
    user = get_current_user(access_token)
    result = canvas_repository.get_canvas(user["id"], canvas_id)
    return result


@router.post("/create_canvas", response_model=ServerResponse)
def create_canvas(data: CanvasDataToCreate):
    '''
    Create a new empty Canvas table
    '''
    user = get_current_user(data.access_token)
    result = canvas_service.create_canvas(data, user["id"])
    return result


@router.delete("/delete_canvas", response_model=ServerResponse)
def delete_canvas(access_token: str, canvas_id: str):
    user = get_current_user(access_token)
    result = canvas_service.delete_canvas(user["id"], canvas_id)
    return result


@router.post("/update_canvas", response_model=ServerResponse)
def delete_canvas(data: CanvasDataToUpdate):
    user = get_current_user(data.access_token)
    result = canvas_service.update_canvas(data, user["id"])
    return result


@router.post("/create_canvas_template", response_model=ServerResponse)
def create_canvas_template(canvasTemplateData: CanvasTemplateToCreate):
    '''
    Create a new template of Canvas table
    '''
    user = check_for_admin(canvasTemplateData.access_token)

    result = canvas_service.create_canvas_template(canvasTemplateData)
    return result


@router.delete("/delete_canvas_template", response_model=ServerResponse)
def delete_canvas_template(access_token: str, canvas_type: str):
    user = check_for_admin(access_token)

    result = canvas_service.delete_canvas_template(canvas_type)
    return result


@router.get("/canvas_templates", response_model=ServerResponse)
def get_canvas_templates(access_token: str):
    result = canvas_repository.get_canvas_templates()
    return {
        "code": 0,
        "message": {
            "data": result
        }
    }

@router.post("/send_canvas_to_mail")
def send_canvas_to_mail(data: CanvasDataToSend):
    isItSpam = check_data_for_spam(data)
    if (isItSpam != True):
        send_mail(data)
    else:
        return {
            "code": 1,
            "message": "spam"
        }