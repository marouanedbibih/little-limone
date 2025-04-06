from rest_framework.exceptions import APIException
from rest_framework import status

class BusinessException(APIException):
    status_code = None
    default_detail = "A business exception occurred"
    field_errors = None
    error_details = None

    def __init__(self, message=None, field_errors=None, error_details=None, status_code=None):
        if message:
            self.detail = message
        if field_errors:
            self.field_errors = field_errors
        if error_details:
            self.error_details = error_details
        if status_code:
            self.status_code = status_code
        super().__init__(self.detail)
    
    def to_dict(self):
        error_response = {
            "message": self.detail,
            "status_code": self.status_code,
        }
        if self.field_errors:
            error_response["field_errors"] = [field_error.to_dict() for field_error in self.field_errors]
        if self.error_details:
            error_response["error_details"] = self.error_details
        return error_response

class FieldError:
    def __init__(self, field, message):
        self.field = field
        self.message = message

    def to_dict(self):
        return {"field": self.field, "message": self.message}
