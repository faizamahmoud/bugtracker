from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationLoginLogoutTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register(self):
        url = reverse('register')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_login(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')

        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_logout(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Login the user
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        self.client.post(url, data, format='json')

        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
