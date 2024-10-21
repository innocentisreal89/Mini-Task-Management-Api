from rest_framework import serializers
from .models import Todo
# from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer


# class UserCreateSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         fields = ["id","email","name","password"]

# class CurrentUserSerializer(UserSerializer):
#     class Meta(UserSerializer.Meta):
#         fields = ["id","email","name","password"]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields =["id","task","priority","is_completed","user","date_created", "updated"]


class TodoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields =["id","task","priority","is_completed","date_created", "updated"]

    

