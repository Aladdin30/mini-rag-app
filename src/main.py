from fastapi import FastAPI
from routes import base,data,nlp
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from stores.llm.LLMProviderFactory import LLMPRoviderFactory
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory

app=FastAPI()


async def startup_span():
    setting=get_settings()
    app.mongo_conn =AsyncIOMotorClient(setting.MONGODB_URL)
    app.db_client =app.mongo_conn[setting.MONGODB_DATABASE]

    llm_provider_factory=LLMPRoviderFactory(setting)
    vectordb_provider_factory=VectorDBProviderFactory(setting)
    #generation client
    app.generation_client= llm_provider_factory.create(provider=setting.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id=setting.GENERATION_MODEL_ID)
    #embedding client
    app.embedding_client= llm_provider_factory.create(provider=setting.EMBEDDING_BECKEND)
    app.embedding_client.set_generation_model(model_id=setting.GENERATION_MODEL_ID)
                                              #embedding_size=setting.EMBEDDING_MODEL_SIZE)
    app.vectordb_client= vectordb_provider_factory.create(provider=setting.VECTOR_DB_BACKEND)
    app.vectordb_client.connect()

async def shutdown_span():
    app.mongo_conn.close()
    app.vectordb_client.connect()

 
app.on_event("startup")(startup_span)
app.on_event("shutdown")(shutdown_span)

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)