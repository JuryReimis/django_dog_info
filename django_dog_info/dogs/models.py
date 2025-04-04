from django.db import models


class Dog(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name="Кличка"
    )

    age = models.PositiveIntegerField(
        verbose_name="Возраст"
    )

    breed = models.ForeignKey(
        to='Breed',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='dogs',
        verbose_name="Порода"
    )

    gender = models.CharField(
        max_length=120,
        verbose_name="Пол"
    )

    color = models.CharField(
        max_length=120,
        verbose_name="Цвет"
    )

    favorite_food = models.CharField(
        max_length=120,
        verbose_name="Любимая еда"
    )

    favorite_toy = models.CharField(
        max_length=120,
        verbose_name="Любимая игрушка"
    )

    def __str__(self):
        return

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"


class Breed(models.Model):

    TINY = '0'
    SMALL = '1'
    MEDIUM = '2'
    LARGE = '3'

    SIZES = (
        (TINY, "Tiny"),
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large")
    )

    POWER_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    name = models.CharField(
        max_length=120,
        verbose_name="Название"
    )

    size = models.CharField(
        max_length=1,
        choices=SIZES,
        verbose_name="Размер"
    )

    friendliness = models.PositiveSmallIntegerField(
        choices=POWER_CHOICES,
        verbose_name="Дружелюбность"
    )

    trainability = models.PositiveSmallIntegerField(
        choices=POWER_CHOICES,
        verbose_name="Способность к тренировкам"
    )

    shedding_amount = models.PositiveSmallIntegerField(
        choices=POWER_CHOICES,
        verbose_name="Объем линьки"
    )

    exercise_needs = models.PositiveSmallIntegerField(
        choices=POWER_CHOICES,
        verbose_name="Потребность в активных действиях"
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
