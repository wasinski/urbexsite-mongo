import pytest
from ..factories import UserFactory
from ..serializers import UserCreationSerializer


@pytest.mark.django_db
class UserCreationSerializerTests:

    @pytest.fixture(scope='class')
    def data(self, request):
        user = UserFactory.build()
        data = {
            'email': user.email,
            'username': user.username,
            'password': 'Pass12#$%',
            'confirm_password': 'Pass12#$%',
        }
        return data

    def test_user_creation_success(self, data):
        serializer = UserCreationSerializer(data=data)
        assert serializer.is_valid()

    def test_serializer_invalid(self, data):
        data['email'] = 'invalidemail'
        serializer = UserCreationSerializer(data=data)
        assert not serializer.is_valid()

    def test_serializer_validator(self, data):
        data['password'] = 'pass'  # password is too short
        data['confirm_password'] = 'pass'
        serializer = UserCreationSerializer(data=data)
        assert not serializer.is_valid()
