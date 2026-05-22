from .BaseController import BaseController
from models.db_schemes import Project,DataChunk
from typing import List
from stores.llm.LLMEnums import DocumentTypeEnums

class NLPController(BaseController):
    def __init__(self,vectordb_clien, embedding_client, generation_client):
        super().__init__()
        
        self.vectordb_clien = vectordb_clien
        self.embedding_client = embedding_client
        self.generation_client = generation_client

    def create_collection_name(self,project_id:str):
        return f"collection_{project_id}".strip()
    
    def reset_vector_db_collection(self,project:Project):
        collection_name = self.create_collection_name(project_id=project.project_id)
        return self.vectordb_clien.delete_collection(collection_name=collection_name)
    
    def get_vector_db_collection_info(self,project:Project):
        collection_name = self.create_collection_name(project_id=project.project_id)
        collection_info= self.vectordb_clien.get_collection_info(collection_name=collection_name)
        return collection_info
    
    def index_into_vector_db(self,project:Project,datachunk:List[DataChunk],do_reset:bool =False):
        #step 1:creat collection name
        collection_name = self.create_collection_name(project_id=project.project_id)

        #step 2:manage items
        texts=[c.chunk_text for c in datachunk]
        metadatas=[c.chunk_metadata for c in datachunk]
        vectors= [ self.embedding_client.embed_text(text=text,
                    document_type=DocumentTypeEnums.DOCUMENT.value)
                    for text in texts]
        
        #step 3:create collection if not exists
        _= self.vectordb_clien.create_collection(
            collection_name=collection_name,
            embedding_size=self.embedding_client.embedding_size,
            do_reset=do_reset)
        
        #step 4:insert into database
        _= self.vectordb_clien.insert_many(
            collection_name=collection_name,
            texts=texts,
            vector=vectors,
            metadata=metadatas )
        return True



    


