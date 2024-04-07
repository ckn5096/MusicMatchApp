

# from django.contrib.auth.password_validation import validate_password
# from rest_framework import serializers
# #from .models import CustomUser
# from django.contrib.auth.models import User
#
# class RegistrationSerializer(serializers.ModelSerializer):
#    # password = serializers.CharField(write_only=True, validators=[validate_password])
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}
#
#         def create(self, validated_data):
#             user = User.objects.create_user(
#                 first_name=validated_data['first_name'],
#                 last_name=validated_data['last_name'],
#                 username=validated_data['username'],
#                 email=validated_data['email'],
#                 password=validated_data['password']
#             )
#             return user

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        user = User.objects.create(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if not user or not user.is_active:
            raise serializers.ValidationError("Incorrect credentials")
        return user

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
       # fields = ['username', 'email', 'first_name', 'last_name']  # Add fields that can be updated
        fields = ['username']  # Add fields that can be updated

    def validate_username(self, value):
        """
        Check if the username is unique, excluding the current user.
        """
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError("This username is already in use.")
        return value

    def update(self, instance, validated_data):
        """
        Update the user profile with the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        #instance.password = validated_data.get('password', instance.password)
        #instance.email = validated_data.get('email', instance.email)
        #instance.first_name = validated_data.get('first_name', instance.first_name)
        #instance.last_name = validated_data.get('last_name', instance.last_name)
        #instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance