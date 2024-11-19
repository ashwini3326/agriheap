from fastapi import FastAPI
from app.api import farmer_router, crop_router
from app.db.database import engine, Base
from app.core.config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, version=settings.app_version)

# Include API router
app.include_router(farmer_router.router, prefix="/v1/farmer", tags=["farmers"])
app.include_router(crop_router.router, prefix="/v1/crop", tags=["crops"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Crop Yield Management System"}