from rest_framework import serializers

from .models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    r"""Базовый сериализатор для модели Breed

        Наследуется от стандартного ModelSerializer. Добавлены поля для отображения size_display и количества
        собак с такой же породой."""
    size_display = serializers.SerializerMethodField(read_only=True)

    same_breed_dogs_count = serializers.IntegerField(read_only=True)

    @staticmethod
    def get_size_display(obj: Breed):
        return obj.get_size_display()

    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'size_display', 'friendliness', 'trainability', 'shedding_amount',
                  'exercise_needs', 'same_breed_dogs_count']


class DogSerializer(serializers.ModelSerializer):
    r"""Базовый сериализатор для модели Dog.

        Наследуется от стандартного ModelSerializer.
        Добавлено отображение развернутых данных для породы, среднего возраста у собак данной породы,
        количество собак с такой породой и gender_display поля."""
    breed_data = BreedSerializer(source='breed', read_only=True)

    avg_age = serializers.FloatField(read_only=True)

    same_breed_count = serializers.IntegerField(read_only=True)

    gender_display = serializers.SerializerMethodField()

    @staticmethod
    def get_gender_display(obj: Dog):
        return obj.get_gender_display()

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'breed_data', 'avg_age', 'same_breed_count', 'color', 'gender',
                  'gender_display']
