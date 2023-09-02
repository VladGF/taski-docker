"""Serializers - Django REST framework."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializers модели Task."""

    class Meta:
        """Метаданные модели Task."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
