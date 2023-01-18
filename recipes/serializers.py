from rest_framework import serializers
from .models import DishCategory
from .models import Dish
import dishes.recipes.views

class DishCategorySerializer(serializers.HyperlinkedModelSerializer):
    dishes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='dish-detail'
    )

    class Meta:
        model = DishCategory
        fields = (
            'url',
            'pk',
            'name',
            'dishes'
        )


class DishSerializer(serializers.HyperlinkedModelSerializer):
    dish_category = serializers.SlugRelatedField(queryset=DishCategory.objects.all(), slug_field='name')

    class Meta:
        model = Dish
        fields = (
            'url',
            'name',
            'dish_category',
            'description',
            'ingredients',
            'recipe',
            'post_date',
            'difficulty_1_10',
            'created'

        )

