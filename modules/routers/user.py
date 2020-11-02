from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def login():
  return "user"