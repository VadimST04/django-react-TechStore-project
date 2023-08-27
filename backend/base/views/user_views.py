from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from base.serializers import UserSerializer, UserSerializerWithToken, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    """
    This view extends the TokenObtainPairView from the SimpleJWT library to use a custom view
    for obtaining authentication tokens.
    serializer_class: MyTokenObtainPairSerializer is a custom serializers.
    """

    serializer_class = MyTokenObtainPairSerializer


class UserAPIView(APIView):
    """
    View for handling user data.
    This view is designed to retrieve a list of all users and is accessible only to admin users.
    """

    permission_classes = (IsAdminUser,)

    def get(self, request):
        """
        Handle GET requests for the view.
        :param request: An HTTP request object.
        :return:  Returns list of all users.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileAPIView(APIView):
    """
    View for handling user profile data.
    This view provides functionality for retrieving and updating user profile information.
    The view is accessible only for authenticated users.
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Handle GET requests for the view.
        :param request: An HTTP request object.
        :return: Returns the profile information of the authenticated user
        """
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Handle PUT requests for the view.
        :param request: An HTTP request object.
        :return: pdates user information and returns the updated profile.
        """
        user = request.user
        serializer = UserSerializerWithToken(user)

        data = request.data

        user.first_name = data['name']
        user.username = data['email']
        user.email = data['email']

        if not data['password']:
            user.password = make_password(data['password'])

        user.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegisterAPIView(APIView):
    """
    View for registering new users.
    """

    def post(self, request):
        """
        Handle POST requests for the view.
        :param request: An HTTP request object.
        :return: Returns information about the new user along with an access token if the user has not been
        previously registered in the database. If the user with the provided email already exists,
        returns an error message.
        """
        data = request.data
        try:
            user = User.objects.create(
                first_name=data['name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )
            serializer = UserSerializerWithToken(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            message = {'detail': 'user with this email already exist'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
