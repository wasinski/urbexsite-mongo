from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .permissions import UserPermissions
from .serializers import UserCreationSerializer
from .tasks import email_confirmation


class UserCreationFormViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermissions,)
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer

    def create(self, request, *args, **kwargs):
        UserCreationSerializer = self.get_serializer_class()
        user = UserCreationSerializer(data=request.data)

        if user.is_valid():
            instance = user.save()
            instance.save()
            email_confirmation.delay(instance)
            return Response(status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def register_confirm(self, activation_key=None):
    try:
        self.user = User.objects.get(activation_key=activation_key)
        self.user.is_active = True
        self.user.save()
        return Response(status=status.HTTP_200_OK)
    except ValueError:
        return Response(status=status.HTTP_404_NOT_FOUND)
