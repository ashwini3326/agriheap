from fastapi import APIRouter
from app.api.v1.endpoints import crop, yield

api_router = APIRouter()
api_router.include_router(crop.router, prefix="/crops", tags=["crops"])
api_router.include_router(yield.router, prefix="/yields", tags=["yields"])