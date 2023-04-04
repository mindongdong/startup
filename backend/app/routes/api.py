from fastapi import APIRouter
from app.routes.endpoints import matches, tracking

api_router = APIRouter()

api_router.include_router(matches.router, prefix="/matches", tags=["matches"])
api_router.include_router(tracking.router, prefix="/tracking", tags=["tracking"])