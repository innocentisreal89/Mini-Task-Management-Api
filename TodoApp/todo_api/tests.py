from django.test import TestCase
from users.models import UserData
from rest_framework.test import APIClient
from todo_api.models import Todo
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# Create your tests here.


class TodoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        


# Testing Models
# class TodoModel(TodoTestCase):
#     def test_todo(self):
#         self.assertEqual(str(self.__str__), 'str')

# Testing Endpoints
class TodoRoutes(TodoTestCase):
    #1  Retrieve all Todos
    def test_get_all_todo(self):
        user = UserData.objects.create(name='john', email='johndoe12@gmail.com', password='js')
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get('/todo/api')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #2  Retrieve a Todo
    def test_get_todo(self):
        user = UserData.objects.create(name='john', email='johndoe12@gmail.com', password='js')
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get('/todo/api/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # #3  Create a Todo
    # def test_post_todo(self):
    #     user = UserData.objects.create(name='john', email='johndoe12@gmail.com', password='js')

    #     data = {
    #         'task':'cook food for the dogs',
    #         'priority':'H',
    #         'user': user.id,
    #     }
    #     refresh = RefreshToken.for_user(user)
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    #     response = self.client.post('/todo/api',data=data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    # #4  Update a Todo
    # def test_put_todo(self):
    #     data = { 
    #         'task':'cook food for the dogs',
    #         'priority':'L',
    #         'is_completed':'True'
    #     }
    #     response = self.client.put('/todo/api/1',data=data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
