from rest_framework import generics
from .models import Moto
from .serializers import MotoSerializer


class MotoList(generics.ListCreateAPIView):
    queryset = Moto.ojects.all()  # when you call the API, you will get all of the motos
    serializer_class = MotoSerializer


class MotoDetail(generics.RetrieveUpdateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    