from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


User = get_user_model()


class UserCreateTests(TestCase):

    def setUp(self):
        self.user_client = Client()

    def test_create_user_not_true(self):
        """Проверка что создается"""
        users_count = User.objects.count()
        print('users' + str(users_count))
        form_data = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'emplyooo',
            'email': 'emplyooo@gmail.com',
            'password1': '12345678900987654321',
            'password2': '12345678900987654321',
        }
        response = self.user_client.post(
            reverse('users:signup'),
            data=form_data,
            follow=True
        )
        t = User.objects.count()
        print('peremennaya', response.status_code, t)
        self.assertEqual(User.objects.count(), users_count)
        self.assertEqual(response.status_code, 200)
