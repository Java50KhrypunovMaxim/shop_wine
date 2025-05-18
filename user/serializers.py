from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password", "address",)
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 8,
                "<PASSWORD>": True},
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)