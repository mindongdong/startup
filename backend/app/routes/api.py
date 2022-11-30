from fastapi import APIRouter
from app.routes.endpoints import matches

api_router = APIRouter()

api_router.include_router(matches.router, prefix="/matches", tags=["matches"])