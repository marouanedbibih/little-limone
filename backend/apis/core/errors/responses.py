class ErrorResponse:
    def __init__(self, message, status_code, field_errors=None, error_details=None):
        self.message = message
        self.status_code = status_code
        self.field_errors = field_errors or []
        self.error_details = error_details or []

    def to_dict(self):
        return {
            "message": self.message,
            "status_code": self.status_code,
            "field_errors": [field_error.to_dict() for field_error in self.field_errors],
            "error_details": self.error_details
        }
