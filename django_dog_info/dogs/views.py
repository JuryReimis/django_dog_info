from django.db.models import OuterRef, Avg, Subquery
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedsViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DogsViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.select_related('breed')
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        subquery = Dog.objects.filter(breed=OuterRef('breed')).values('breed').annotate(avg_age=Avg('age')).values(
            'avg_age')

        dogs = Dog.objects.select_related('breed').annotate(avg_age=Subquery(subquery))
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)
