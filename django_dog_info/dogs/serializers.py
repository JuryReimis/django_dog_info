from rest_framework import serializers

from .models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs']


class DogSerializer(serializers.ModelSerializer):

    gender_display = serializers.SerializerMethodField()

    @staticmethod
    def get_gender_display(obj: Dog):
        return obj.get_gender_display()

    class Meta:
        model = Dog
        fields = ['name', 'age', 'breed', 'color', 'gender', 'gender_display']
