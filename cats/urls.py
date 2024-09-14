from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet

# Создаем маршрутизатор, который автоматически создаст маршруты для нашего ViewSet
router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cat')


urlpatterns = [
    path('', include(router.urls)),  # Включаем все маршруты, сгенерированные роутером
]