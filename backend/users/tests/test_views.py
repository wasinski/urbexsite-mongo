import json
import pytest

from configuration.celery import app
from django.core import mail
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from ..factories import UserFactory


User = get_user_model()
client = APIClient()


@pytest.mark.django_db
class UserCreationTests:

    @pytest.fixture
    def payload(self, request):
        return {
            'username': 'test_user',
            'email': 'test@example.com',
            'password1': 'Pass12#$%',
            'password2': 'Pass12#$%',
        }

    @pytest.fixture
    def registration(self, request):
        return '/api/accounts/registration/'

    def test_success_user_creation(self, payload, registration):
        response = client.post(registration, payload)
        assert response.status_code is status.HTTP_201_CREATED
        assert User.objects.count() == 1

    def test_failed_user_creation(self, payload, registration):
        payload['email'] = 'this aint a valid email'
        response = client.post(registration, payload)
        assert response.status_code is status.HTTP_400_BAD_REQUEST
        assert User.objects.count() == 0

    def test_send_email(self, payload, registration):
        response = client.post(registration, payload)
        assert response.status_code is status.HTTP_201_CREATED
        assert len(mail.outbox) == 1


@pytest.mark.django_db
class UserLoginTests:

    @pytest.fixture
    def payload(self, request):
        return {
            'username': 'test_user',
            'password': 'Password123$%^',
        }

    @pytest.fixture
    def login(self, request):
        return '/api/accounts/login/'

    def test_success_auth_user(self, login, payload):
        User.objects.create_user(email='example@abc.com', **payload)
        response = client.post(login, payload)
        assert response.status_code is status.HTTP_200_OK, response.data

    def test_failed_auth_user(self, login, payload):
        User.objects.create_user(email='example@abc.com', **payload)
        payload['password'] = 'invalidpassword'
        response = client.post(login, payload)
        assert response.status_code is status.HTTP_400_BAD_REQUEST, response.data


@pytest.mark.django_db
class UserDetailsViewPermissionTests:

    @pytest.fixture
    def user_details(self, request):
        return '/api/accounts/user/'

    @pytest.fixture
    def auth_client(self, request):
        user = User.objects.create(email='a@abc.com', password='123', username='abc')
        client.force_login(user)
        yield client
        client.logout()

    def test_authenticated_user_details(self, user_details, auth_client):
        response = auth_client.get(user_details)
        assert response.status_code is status.HTTP_200_OK

    def test_not_authenticated_user_details(self, user_details):
        self.another_user = UserFactory.create()
        response = client.get(user_details)
        assert response.status_code is status.HTTP_403_FORBIDDEN
