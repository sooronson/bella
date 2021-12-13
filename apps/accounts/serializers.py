from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'phone_number',
            'password',
            'password2',
            'first_name',
            'last_name'
        )

    def validate(self, attrs):
        password2 = attrs['password2']
        if attrs.get('password') != password2:
            raise serializers.ValidationError('Your passwords must be same!!!')
        if not attrs.get('password').isalnum():
            serializers.ValidationError('You can use only letters and numbers for your password')
        phone_number = attrs.get('phone_number')
        user = authenticate(username=phone_number, password=password2)
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

