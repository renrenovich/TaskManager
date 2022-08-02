from django.db import models

# Create your models here.


class Tasks(models.Model):
    """Модель задач"""
    title = models.CharField(unique=True, max_length=128, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    is_done = models.BooleanField(default=False, verbose_name='Задача выполнена')
    date_of_start = models.DateField(auto_now_add=True, verbose_name='Задача выдана')
    date_of_end = models.DateField(verbose_name='Завершить до')
