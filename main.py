from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from canvas.modules.auth import auth_repository
from canvas.modules.routers import auth, user, test
from canvas.utils.exceptions import ResponseException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(ResponseException)
async def response_exception_handler(request: Request, exp: ResponseException):
    return JSONResponse(
        status_code=exp.status_code,
        content={
            "code": exp.error_code,
            "message": exp.message
        }
    )

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(test.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
