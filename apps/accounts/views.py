from rest_framework import status, generics

from .serializers import RegisterSerializer
from .models import CustomUser


class RegisterApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


