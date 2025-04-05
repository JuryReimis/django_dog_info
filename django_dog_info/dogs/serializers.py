from rest_framework import serializers

from .models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    size_display = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_size_display(obj: Breed):
        return obj.get_size_display()

    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'size_display', 'friendliness', 'trainability', 'shedding_amount',
                  'exercise_needs']


class DogSerializer(serializers.ModelSerializer):
    breed_data = BreedSerializer(source='breed', read_only=True)

    avg_age = serializers.FloatField(read_only=True)

    gender_display = serializers.SerializerMethodField()

    @staticmethod
    def get_gender_display(obj: Dog):
        return obj.get_gender_display()

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'breed_data', 'avg_age', 'color', 'gender', 'gender_display']
