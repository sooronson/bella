from rest_framework import generics

from .serializers import AboutSerializer, ContactSerializer
from .models import About, Contact


class AboutView(generics.RetrieveAPIView):
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()


class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
