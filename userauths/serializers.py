from .models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "full_name", "password", "password2", "phone"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            phone=validated_data["phone"],
        )
        email_user, _ = validated_data["email"].split("@")
        user.username = email_user
        user.set_password(validated_data["password"])
        user.save()
        return user
