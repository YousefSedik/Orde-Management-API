from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            # Authenticate using email and password
            user = authenticate(
                request=self.context.get("request"), username=email, password=password
            )
            if not user:
                msg = "Unable to log in with provided credentials."
                raise serializers.ValidationError(msg, code="authorization")

        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        user = validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return token
