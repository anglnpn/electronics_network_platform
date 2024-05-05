# from django.shortcuts import render
#
# from rest_framework import generics
# from users.models import User
# from users.paginators import UserPagination
# from users.serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.hashers import make_password
#
#
# class UserCreateAPIView(generics.CreateAPIView):
#     """
#     Cоздание пользователя
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#     def perform_create(self, serializer):
#         """
#         Хэширование пароля перед
#         сохранением пользователя.
#         """
#         validated_data = serializer.validated_data
#         password = validated_data.get('password')
#         hashed_password = make_password(password)
#         serializer.save(password=hashed_password)
#
#
# class UserListAPIView(generics.ListAPIView):
#     """
#     Просмотр списка пользователей
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#     pagination_class = UserPagination
#
#
# class UserRetrieveAPIView(generics.RetrieveAPIView):
#     """
#     Просмотр одного пользователя
#     """
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated]
#
#
# class UserUpdateAPIView(generics.UpdateAPIView):
#     """
#     Изменение пользователя
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated]
#
#
# class UserDestroyAPIView(generics.DestroyAPIView):
#     """
#     Удаление пользователя
#     """
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated]
