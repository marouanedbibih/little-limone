from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from .models import User
from core.errors.exceptions import BusinessException, FieldError


class UserView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data

                user = User.objects.create_user(
                    email=validated_data['email'],
                    password=validated_data['password'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    username=validated_data['username'],
                    phone=validated_data['phone']
                )

                return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

            except BusinessException as exc:
                return Response(exc.to_dict(), status=exc.status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
