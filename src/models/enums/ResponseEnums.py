from enum import Enum


class ResponseSignal(Enum):

   
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_TYPE_NOT_ALLOWED = "file type not allowed"
    FILE_SIZE_EXCEEDED = "file size exceeded"
    FILE_UPLOAD_FAILED = "file upload failed"
    FILE_UPLOAD_SUCCESS = "file upload success"
    FILE_UPLOAD_ERROR = "file upload error"
    FILE_VALIDATION_ERROR = "file validation error"
    FILE_VALIDATION_SUCCESS = "file validation success"
    PROCESSING_SUCCESS = "processing_success"
    PROCESSING_FAILED = "processing_failed"

    
    
