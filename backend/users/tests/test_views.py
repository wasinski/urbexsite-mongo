import json
import pytest

from configuration.celery import app
from django.core.urlresolvers import reverse
from django.core import mail
from rest_framework import status
from rest_framework.test import APIClient
from ..factories import UserFactory
from ..models import User


client = APIClient()


@pytest.mark.django_db
class UserCreationTests:

    @pytest.fixture(autouse=True)
    def setUp(self):
        app.conf.CELERY_ALWAYS_EAGER = True

        self.user = UserFactory.build()
        self.data = {
            'email': self.user.email,
            'username': self.user.username,
            'password': 'Pass12#$%',
            'confirm_password': 'Pass12#$%',
        }

    def test_success_user_creation(self):
        response = client.post(reverse('user-list'), self.data, format='json')
        assert response.status_code is status.HTTP_201_CREATED
        assert User.objects.count() == 1

    def test_failed_user_creation(self):
        self.data['email'] = 'invalidemail'
        response = client.post(reverse('user-list'), self.data, format='json')
        assert response.status_code is status.HTTP_400_BAD_REQUEST
        assert User.objects.count() == 0

    def test_send_email(self):
        response = client.post(reverse('user-list'), self.data, format='json')
        assert mail.outbox[0].subject == 'Account confirmation!'

    def test_mail_activation(self):
        self.user = UserFactory.create()
        response = client.get(reverse('activation', args=[self.user.activation_key]), follow=True,
                              content_type='application/json')
        assert response.status_code is status.HTTP_200_OK, response.data

    def test_mail_activation_with_wrong_key(self):
        self.user = UserFactory.create()
        self.user.activation_key = '123wrongkey456'
        response = client.get(reverse('activation', args=[self.user.activation_key]), follow=True,
                              content_type='application/json')
        assert response.status_code is status.HTTP_404_NOT_FOUND, response.data


@pytest.mark.django_db
class UserLoginTests:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.user = UserFactory.create()
        self.data = {
            'email': self.user.email,
            'password': 'pass',
        }

        self.url = reverse('token-auth')

    def test_success_auth_user(self):
        response = client.post(self.url, self.data, format='json')
        assert response.status_code is status.HTTP_200_OK, response.data

    def test_failed_auth_user(self):
        self.data['password'] = 'invalidpassword'
        response = client.post(self.url, self.data, format='json')
        assert response.status_code is status.HTTP_400_BAD_REQUEST, response.data


@pytest.mark.django_db
class UserViewPermissionTests:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.user = UserFactory.create()
        self.data = {
            'email': self.user.email,
            'password': 'pass',
        }
        self.url = reverse('token-auth')
        assert client.login(email=self.user.email, password='pass')

    def test_authenticated_user_details(self):
        response = client.get(reverse('user-detail', args=[self.user.pk]), follow=True,
                              content_type='application/json')
        assert response.status_code is status.HTTP_200_OK
        assert response.data['username'] == self.user.username

    def test_not_authenticated_user_details(self):
        self.another_user = UserFactory.create()
        response = client.get(reverse('user-detail', args=[self.user.pk]), follow=True,
                              content_type='application/json')
        assert response.status_code is status.HTTP_200_OK
        assert response.data['username'] != self.another_user.username


@pytest.mark.django_db
class UserViewSetTests:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.user_one = UserFactory.create()
        self.user_two = UserFactory.create()
        self.user_three = UserFactory.create()

    def test_users_list(self):
        response = client.get(reverse('user-list'), follow=True, content_type='application/json')
        assert response.status_code is status.HTTP_200_OK
        assert len(response.data) == User.objects.all().count()

    def test_invalid_user(self):
        response = client.get(reverse('user-detail', args=['5']), follow=True,
                              content_type='application/json')
        assert response.status_code is status.HTTP_404_NOT_FOUND  # user not found
