from rest_framework.views import exception_handler
from rest_framework.response import Response
from .exceptions import BusinessException, FieldError
from rest_framework.exceptions import MethodArgumentNotValidException

def custom_exception_handler(exc, context):
    """
    Custom exception handler for handling all the exceptions globally
    """
    # Call default exception handler first
    response = exception_handler(exc, context)

    if isinstance(exc, MethodArgumentNotValidException):
        # Format the validation errors in the required format
        field_errors = []
        
        # Iterate over the fields and messages to construct the custom format
        for field, messages in exc.detail.items():
            for message in messages:
                field_errors.append(FieldError(field=field, message=message).to_dict())
        
        return Response({
            "message": "Validation failed",
            "field_errors": field_errors
        }, status=exc.status_code)

    return response
