from fastapi import FastAPI
from routes import base,data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
app=FastAPI()
# on_event every time we run fast api the database will start auto
#app in every routes will see the database
@app.on_event("startup")
async def startup_db_client():
    setting=get_settings()
    app.mongo_conn =AsyncIOMotorClient(setting.MONGODB_URL)
    app.db_client =app.mongo_conn[setting.MONGODB_DATABASE]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()

app.include_router(base.base_router)

app.include_router(data.data_router)
