from rest_framework import viewsets

from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedsViewSet(viewsets.ModelViewSet):

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DogsViewSet(viewsets.ModelViewSet):

    queryset = Dog.objects.select_related('breed')
    serializer_class = DogSerializer

