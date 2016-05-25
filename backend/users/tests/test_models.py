import pytest
from ..factories import UserFactory
from ..models import User


@pytest.mark.django_db
class UserManagerTests:

    def test_superuser_creation(self):
        User.objects.create_superuser(email='admin@gmail.com', password='Pass12#$%')
        assert User.objects.count() == 1

    def test_user_creation(self):
        User.objects.create(
            email='test_user@gmail.com',
            username='test_user',
            password='Pass12#$%'
        )
        assert User.objects.count() == 1

    def test_model_str(self):
        user = UserFactory.create()
        assert str(user) == user.email
