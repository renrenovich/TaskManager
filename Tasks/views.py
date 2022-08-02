from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from Tasks.models import Tasks
from Tasks.serializers import TaskSerializer, CreateTaskSerializer, DoneTaskSerializer


class TaskListView(APIView):
    """Отображение списка всех задач"""

    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class CreateTaskView(generics.CreateAPIView):
    """Создание задачи"""
    serializer_class = CreateTaskSerializer


class SingleTaskView(APIView):
    """Отображение одной здачи"""
    def get(self, request, pk):
        try:
            task = Tasks.objects.get(id=pk)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class DoneTaskView(APIView):
    """Изменение статуса задачи на 'Выполнено'"""
    def get(self, request, pk):
        try:
            task = Tasks.objects.get(id=pk)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            task = Tasks.objects.get(id=pk)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DoneTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteTaskView(APIView):
    """Удаление задачи"""
    def get(self, request, pk):
        try:
            task = Tasks.objects.get(id=pk)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            task = Tasks.objects.get(id=pk)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
