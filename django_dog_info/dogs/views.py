from django.db.models import OuterRef, Avg, Subquery, Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedsViewSet(viewsets.ModelViewSet):
    r"""ViewSet для работы с моделью Breed.

        Используется, как наследник стандартного ModelViewSet.
        Переопределен метод list(), отвечающий за отображение списка экземпляров, которые запрошены по
        \api\breeds\
        GET \api\breeds\ - получение списка пород
        POST \api\breeds\ - создание новой записи по предоставленным данным
        GET \api\breeds\<id>\ - получение записи по id
        PUT \api\breeds\<id>\ - обновление записи по id
        DELETE \api\breeds\<id>\ - удаление записи по id

        При попытке обращения к несуществующему id - "No Breed matches the given query."
        Возможных исключений не обнаружено. Все работает предсказуемо.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def list(self, request, *args, **kwargs):
        breeds = Breed.objects.annotate(
            same_breed_dogs_count=Count('dogs')  # Здесь это корректно
        )
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)


class DogsViewSet(viewsets.ModelViewSet):
    r"""ViewSet для работы с моделью Dog

        Используется как наследник стандартного ModelViewSet.
        Переопределены методы list, для отображения списка собак, и retrieve для отображения экземпляра модели
        по id.
        GET \api\dogs\ - получение списка собак
        POST \api\dogs\ - создание новой записи по предоставленным данным
        GET \api\dogs\<id>\ - получение записи по id
        PUT \api\dogs\<id>\ - обновление записи по id
        DELETE \api\dogs\<id>\ - удаление записи по id

        При запросе к несуществующему id будет возвращено сообщение "No Dog matches the given query."
        При попытке заменить породу на несуществующую - "Invalid pk - object does not exist."
        Возможных исключений не обнаружено. Все работает предсказуемо.
        """
    queryset = Dog.objects.select_related('breed')
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        subquery = Dog.objects.filter(breed=OuterRef('breed')).values('breed').annotate(avg_age=Avg('age')).values(
            'avg_age')

        dogs = Dog.objects.prefetch_related('breed').annotate(avg_age=Subquery(subquery))
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        subquery = Dog.objects.filter(breed=OuterRef('breed')).values('breed').annotate(count=Count('id')).values(
            'count')
        dog = get_object_or_404(Dog.objects.filter(pk=pk).annotate(same_breed_count=Subquery(subquery)))
        serializer = DogSerializer(dog)
        return Response(serializer.data)
