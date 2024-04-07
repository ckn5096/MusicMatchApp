<<<<<<< HEAD
from django.contrib.auth import get_user_model, authenticate, login
=======
from django.contrib.auth import get_user_model , authenticate, login
>>>>>>> origin/master
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
<<<<<<< HEAD
from .serializers import RegistrationSerializer, LoginSerializer, ProfileUpdateSerializer
=======
from .serializers import RegistrationSerializer, LoginSerializer , ProfileUpdateSerializer
>>>>>>> origin/master
from rest_framework.authtoken.models import Token
from django.urls import reverse

from rest_framework.authentication import get_authorization_header
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
import jwt

<<<<<<< HEAD
User = get_user_model()


=======


User = get_user_model()

>>>>>>> origin/master
# Create your views here.

class RegistrationView(APIView):
    permission_classes = [AllowAny]
    queryset = []  # Add this line

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            send_welcome_email(user.email)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_welcome_email(user_email):
    subject = 'Welcome to Your Website'
    message = 'Welcome to Music Match! \nThank you for signing up \n. Please confirm your email address in order to activate your account.'
    from_email = 'music.match.django@gmail.com'

    send_mail(subject, message, from_email, [user_email], fail_silently=True)

<<<<<<< HEAD

=======
>>>>>>> origin/master
# class LoginView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             token, created = Token.objects.get_or_create(user=user)
#
#             home_url = reverse('home')
#
#             print('Generated Token:', token.key)
#
#             return Response({'token': token.key, 'redirect_url': home_url}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            home_url = reverse('home')
            token, created = Token.objects.get_or_create(user=user)
            print('Generated Token:', token.key)
<<<<<<< HEAD
            # return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
=======
            #return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
>>>>>>> origin/master
            return Response({'token': token.key, 'redirect_url': home_url}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Extract the token from the request
        token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

        try:
            # Retrieve the token from the database
            token = Token.objects.get(key=token_key)

            # Get the user associated with the token
            user = token.user

            # Now you have the authenticated user, you can use it as needed
            return Response({'message': f'Welcome, {user.username}!'})
        except Token.DoesNotExist:
            # If the token doesn't exist in the database, it's invalid
            return Response({"error": "Invalid token!!"}, status=status.HTTP_401_UNAUTHORIZED)


# class ProfileUpdateView(APIView):
#     permission_classes = [AllowAny]
#     #permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         serializer = ProfileUpdateSerializer(instance=request.user, data=request.data, partial=True)
#
#         if serializer.is_valid():
#             # Save the updated user information
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


<<<<<<< HEAD
=======

>>>>>>> origin/master
class ProfileUpdateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Retrieve the token from the request headers
        token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        token = Token.objects.get(key=token_key)

<<<<<<< HEAD
=======

>>>>>>> origin/master
        # Now you can use the token for authentication
        # Assuming you have a custom user model with 'username' and 'password' fields
        user = token.user

        # Retrieve data from the request
        new_username = request.data.get('new_username')
        new_password = request.data.get('new_password')
        new_firstname = request.data.get('new_firstname')
        new_lastname = request.data.get('new_lastname')
        new_email = request.data.get('new_email')

        # Update user's username if provided
        if new_username:
            user.username = new_username

        # Update user's password if provided
        if new_password:
            user.set_password(new_password)

        # Update user's firstname if provided
        if new_firstname:
            user.first_name = new_firstname

        # Update user's lastname if provided
        if new_lastname:
            user.last_name = new_lastname

        # Update user's email if provided
        if new_email:
            user.email = new_email

<<<<<<< HEAD
=======

>>>>>>> origin/master
        # Save the updated user
        user.save()

        home_url = reverse('home')

<<<<<<< HEAD
        return Response({'message': 'Profile updated successfully', 'redirect_url': home_url},
                        status=status.HTTP_200_OK)
=======
        return Response({'message': 'Profile updated successfully', 'redirect_url': home_url}, status=status.HTTP_200_OK)

>>>>>>> origin/master
