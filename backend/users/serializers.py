from django.contrib.auth.password_validation import get_default_password_validators
from rest_framework import serializers
from .models import User


class UserCreationSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(allow_blank=False, required=True, write_only=True, )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'confirm_password', )
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        validate_password_strength(data.get('password'))
        if data.get('password') != data.pop('confirm_password'):
            raise serializers.ValidationError('Passwords don\'t match.')
        return data


def validate_password_strength(password):
    password_validators = get_default_password_validators()
    for validator in password_validators:
        validator.validate(password)
