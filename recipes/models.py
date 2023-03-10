from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class DishCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200, blank=False, default='', unique=True)
    dish_category = models.ForeignKey(DishCategory, related_name='dishes', on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True, default='')
    ingredients = models.CharField(max_length=300, blank=False, default='')
    recipe = models.TextField(max_length=1000,  blank=False, default='')
    post_date = models.DateTimeField()
    difficulty_1_10 = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='dishes', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

