from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'username': 'Ivaaaan',
            'email': 'inaniv@mail.ru',
            'password1': '123456Pp',
            'password2': '123456Pp',
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Registration')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, data=self.data)  # Передаем данные в POST-запрос
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('products:home'))
        self.assertTrue(User.objects.filter(username=username).exists())
