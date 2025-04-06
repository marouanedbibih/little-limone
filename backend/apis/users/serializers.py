from .models import User
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password', 'first_name', 'last_name','phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }
