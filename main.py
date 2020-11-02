from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.auth import auth_repository
from modules.routers import auth, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)

# def set_up_project():
#     # user_collection = store.get_collection('User')
#     # auth_repository = auth_repository.AuthRepository(user_collection)
#     store.ping()

# set_up_project()