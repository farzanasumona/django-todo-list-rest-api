from rest_framework.test import APITestCase
from TodoListApp.models import Task
from django.urls import reverse


class BasicTest(APITestCase):

    def test_get_all_todos(self):
        response = self.client.get('/api/v1/tasks/all/')
        self.assertEqual(response.status_code, 200)


class GetViewsTest(APITestCase):

    url = reverse('get_by_id_task', args=[1])

    def test_get_by_id_todos(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)

        task = Task(title='title', is_done=True, desc='desc')
        task.save()

        response = self.client.get(reverse('get_by_id_task', kwargs={'pk': task.pk}), follow=True)
        self.assertEqual(response.status_code, 200)


class DeleteViewsTest(APITestCase):

    url = reverse('get_by_id_task', args=[1])

    def test_delete_by_id_todos(self):

        task = Task(title='title', is_done=True, desc='desc')
        task.save()

        response = self.client.delete(reverse('get_by_id_task', kwargs={'pk': task.pk}), follow=True)
        self.assertEqual(response.status_code, 204)


class UpdateViewsTest(APITestCase):

    url = reverse('get_by_id_task', args=[1])

    def test_put_by_id_todos(self):

        task = Task(title='title', is_done=True, desc='desc')
        task.save()

        data = {

            "title": "ed",
            "is_done": True,
            "desc": "I am working"
        }

        response = self.client.put(reverse('get_by_id_task', kwargs={'pk': task.pk}), data, format='json')
        self.assertEqual(response.status_code, 200)

        task.refresh_from_db()
        self.assertEqual('ed', task.title)

    def test_patch_by_id_todos(self):

        task = Task(title='title', is_done=True, desc='desc')
        task.save()

        data = {

            "title": "patch the title"
        }

        response = self.client.patch(reverse('get_by_id_task', kwargs={'pk': task.pk}), data, format='json')
        self.assertEqual(response.status_code, 200)

        task.refresh_from_db()
        self.assertEqual('patch the title', task.title)


class CreateViewsTest(APITestCase):

    create_url = reverse('create-task')

    def test_create_task_todos(self):
        data = {

            "title": "ed",
            "is_done": True,
            "desc": "I am working"
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, 200)


