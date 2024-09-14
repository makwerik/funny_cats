from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cat(models.Model):
    """Модель кота"""
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)  # Порода
    is_furry = models.BooleanField(default=True)  # Булевое поле для волосатости кота (по умолчанию кот волосатый)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cats')

    def __str__(self):
        return self.name