from rest_framework import serializers
from .models import Cat
from django.contrib.auth.models import User


class CatSerializer(serializers.ModelSerializer):
    """Сериализатор для кота"""
    class Meta:
        model = Cat
        fields = ['id', 'name', 'age', 'breed', 'is_furry', 'owner']
        read_only_fields = ['owner']  # Поле только для чтения, его нельзя изменить


class UserSerializer(serializers.ModelSerializer):
    cats = CatSerializer(many=True, read_only=True)  # Пользователь может иметь несколько котов, все они будут как вложенный объект

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'cats']
