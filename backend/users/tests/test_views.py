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
    def payload(request):
        return {
            'username': 'test_user',
            'email': 'test@example.com',
            'password1': 'Pass12#$%',
            'password2': 'Pass12#$%',
        }

    @pytest.fixture
    def registration(request):
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
    def payload(request):
        return {
            'username': 'test_user',
            'password': 'Password123$%^',
        }

    @pytest.fixture
    def login(request):
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


@pytest.mark.skip("refactoring")
@pytest.mark.django_db
class UserViewPermissionTests:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.user = UserFactory.create()
        self.data = {
            'email': self.user.email,
            'password': 'pass',
        }
        self.registration = reverse('token-auth')
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


@pytest.mark.skip("refactoring")
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
