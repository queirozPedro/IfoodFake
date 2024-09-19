from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import UserProfileExampleSerializer
from users.api.serializers import DiretorSerializer
from users.models import UserProfileExample
from users.models import DiretorProfile

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

class DiretorViewSet(ModelViewSet):
    serializer_class = DiretorSerializer
    permission_classes = [AllowAny]
    queryset = DiretorProfile.objects.all()
    http_method_names = ['get', 'put']