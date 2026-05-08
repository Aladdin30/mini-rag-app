from pydantic import BaseModel,Field
from bson.objectid import Objectid
from typing import Optional


class DataChunk(BaseModel):

    _id:Optional[Objectid]
    chunk_text:str =Field(...,min_length=1)
    chunk_metadata:dict
    chunk_order:int =Field(...,gt=0)
    chunk_project_id: Objectid

   
    class Config:
        arbitrary_types_allowed = True

        