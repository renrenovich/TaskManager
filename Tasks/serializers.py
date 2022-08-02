from rest_framework import serializers

from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор вывода всех задач"""

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'text', 'is_done', 'date_of_start', 'date_of_end']


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['title', 'text', 'date_of_end']


class DoneTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'text', 'is_done', 'date_of_start', 'date_of_end']
        read_only_fields = ['id', 'title', 'text', 'date_of_start', 'date_of_end']

