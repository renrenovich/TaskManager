from django.urls import path
from .views import TaskListView, CreateTaskView, SingleTaskView, DoneTaskView, DeleteTaskView

urlpatterns = [
    path('tasks/', TaskListView.as_view(),name='get_all_tasks'),
    path('tasks/create/', CreateTaskView.as_view(), name='create_task'),
    path('tasks/<int:pk>/', SingleTaskView.as_view(), name='get_single_task'),
    path('tasks/do/<int:pk>/', DoneTaskView.as_view(), name='make_task_done'),
    path('tasks/delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),

]
