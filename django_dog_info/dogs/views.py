from django.db.models import OuterRef, Avg, Subquery, Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedsViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def list(self, request, *args, **kwargs):
        subquery = Dog.objects.filter(breed=OuterRef('id')).values('breed').annotate(
            same_breed_dogs_count=Count('id')).values('same_breed_dogs_count')

        breeds = Breed.objects.annotate(same_breed_dogs_count=Subquery(subquery))
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)


class DogsViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.select_related('breed')
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        subquery = Dog.objects.filter(breed=OuterRef('breed')).values('breed').annotate(avg_age=Avg('age')).values(
            'avg_age')

        dogs = Dog.objects.select_related('breed').annotate(avg_age=Subquery(subquery))
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        subquery = Dog.objects.filter(breed=OuterRef('breed')).values('breed').annotate(count=Count('id')).values(
            'count')
        dog = get_object_or_404(Dog.objects.filter(pk=pk).annotate(same_breed_count=Subquery(subquery)))
        serializer = DogSerializer(dog)
        return Response(serializer.data)
