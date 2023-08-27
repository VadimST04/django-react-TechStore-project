# This is a functional approach for user_views

# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
# from django.db import IntegrityError
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import Response
# from base.serializers import UserSerializer, UserSerializerWithToken
#
#
# @api_view(['POST'])
# def register_user(request):
#     data = request.data
#     try:
#         user = User.objects.create(
#             first_name=data['name'],
#             username=data['email'],
#             email=data['email'],
#             password=make_password(data['password'])
#         )
#         serializer = UserSerializerWithToken(user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     except IntegrityError:
#         message = {'detail': 'user with this email already exist'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_user_profile(request):
#     user = request.user
#     serializer = UserSerializerWithToken(user)
#
#     data = request.data
#
#     user.first_name = data['name']
#     user.username = data['email']
#     user.email = data['email']
#
#     if not data['password']:
#         user.password = make_password(data['password'])
#
#     user.save()
#
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_user_profile(request):
#     user = request.user
#     serializer = UserSerializer(user)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def get_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
