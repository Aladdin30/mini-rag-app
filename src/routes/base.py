from fastapi import FastAPI,APIRouter,Depends
import os
from helpers.config import get_settings,Settings
base_router=APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def home(app_sttings:Settings =Depends(get_settings)):
    
    app_name=app_sttings.APP_NAME
    app_version=app_sttings.APP_VERSION
    return {
        "app_name":app_name,
        "app_version":app_version
    }
