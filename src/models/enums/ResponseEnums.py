from enum import Enum 

class ResponseSignal(Enum):


    FILE_VALIDATED_SUCCESS="file_validata_successfully"
    FILE_TYPES_NOT_SUPPORTED="file_type_not_supported"
    FILE_SIZE_EXCEEDED="file_size_exceeded"
    FILE_UPLOAD_SUCCESS="file_upload_success"
    FILE_UPLOAD_FAILED="file_upload_failed"
    PROCESSING_FAILED="processing_failed"
    PROCESSING_SUCCESS="processing_success"
    NO_FILES_ERROR="no_found_files"
    FILES_ID_ERROR="no_file_found_with_this_id"
    PROJECT_NOT_FOUND_ERROR="project not found error"
    INSERTED_INTO_VECTORDB_ERROR="inserted into vectordb error"
    INSERTED_INTO_VECTORDB_SUCCESS="inserted into vectordb success"
