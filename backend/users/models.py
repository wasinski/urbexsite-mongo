import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):

    def create(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        account = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password):
        account = self.create(email, password)

        account.is_admin = True
        account.is_staff = True
        account.is_superuser = True
        account.is_active = True
        account.save()

        return account


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class User(AbstractBaseUser):

    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(max_length=45, unique=True)
    date_joined = models.DateField(auto_now_add=True, editable=False, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    activation_key = models.UUIDField(default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
