from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.store.init_store import InitStore

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def set_up_project():
    store = InitStore("mongodb+srv://admin:1234@cluster0.wqhlb.azure.mongodb.net/test?retryWrites=true&w=majority")
    store.ping()

set_up_project()