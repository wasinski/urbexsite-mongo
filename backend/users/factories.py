import factory
from .models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@gmail.com' % obj.username)
    gender = ''
    activation_key = '528783d0-e44c-11e5-9730-9a79f06e9478'
    is_active = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', "pass")
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
