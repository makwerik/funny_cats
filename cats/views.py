from rest_framework import viewsets, permissions
from .models import Cat
from .serializers import CatSerializer
from rest_framework.permissions import IsAuthenticated


class CatViewSet(viewsets.ModelViewSet):
    """Предсталвление для работы с моделью Cat"""
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Метод для возвращения тех котов, которые принадлежат текущему пользователю"""
        return Cat.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Метод для создания нового кота, автоматически присваиваем его владельцу"""
        print(f"user: {self.request.user}")
        serializer.save(owner=self.request.user)