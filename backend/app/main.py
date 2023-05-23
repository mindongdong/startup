from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes.api import api_router
from app.common.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME
)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.ROUTES_STR)