from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json

from Tasks.models import Tasks
from Tasks.serializers import TaskSerializer


class AllTasksApiTestCase(APITestCase):
    def test_get(self):
        task_1 = Tasks.objects.create(title='Test task 1', text='test task 1', date_of_end='2022-08-08')
        task_2 = Tasks.objects.create(title='Test task 2', text='test_test task 2', date_of_end='2022-08-10')
        serializer_data = TaskSerializer([task_1, task_2], many=True).data
        response = self.client.get(reverse('get_all_tasks'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class SingleTaskApiTestCase(APITestCase):
    def test_valid_get(self):
        task_1 = Tasks.objects.create(title='Test task 1', text='test task 1', date_of_end='2022-08-08')
        response = self.client.get(reverse('get_single_task', kwargs={'pk': 1}))
        serializer_data = TaskSerializer(task_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_invalid_get(self):
        response = self.client.get(reverse('get_single_task', kwargs={'pk': 10}))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class DeleteTaskApiTestCase(APITestCase):
    def test_valid_delete(self):
        task_1 = Tasks.objects.create(title='Test task 1', text='test task 1', date_of_end='2022-08-08')
        response = self.client.delete(reverse('delete_task', kwargs={'pk': 1}))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_invalid_delete(self):
        response = self.client.delete(reverse('delete_task', kwargs={'pk': 10}))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class UpdateTaskTestCase(APITestCase):
    def test_valid_update(self):
        task_1 = Tasks.objects.create(title='Test task 1', text='test task 1', date_of_end='2022-08-08')
        valid_payload = {
            'is_done': 'true'
        }
        response = self.client.put(reverse('make_task_done',
                                           kwargs={'pk': 1}),
                                           data=json.dumps(valid_payload),
                                           content_type='application/json')
        response1 = self.client.get(reverse('get_single_task', kwargs={'pk': 1}))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_invalid_update(self):
        task_1 = Tasks.objects.create(title='Test task 1', text='test task 1', date_of_end='2022-08-08')
        invalid_payload = {
            'is_done': ''
        }
        response = self.client.put(reverse('make_task_done',
                                           kwargs={'pk': 1}),
                                           data=json.dumps(invalid_payload),
                                           content_type='application/json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)


class CreateTaskTestCase(APITestCase):
    def test_valid_create_task(self):
        valid_payload = {
            'title': 'Test task 1',
            'text': 'Test text 1',
            'date_of_end': '2022-08-08'
        }
        response = self.client.post(reverse('create_task'),
                                      data=json.dumps(valid_payload),
                                      content_type='application/json'
                                      )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_invalid_create_task(self):
        invalid_payload = {
            'title': '',
            'text': 'Test text 1',
            'date_of_end': '2022-08-08'
        }
        response = self.client.post(reverse('create_task'),
                                    data=json.dumps(invalid_payload),
                                    content_type='application/json'
                                    )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
