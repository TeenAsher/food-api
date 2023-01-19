from rest_framework import serializers
from .models import DishCategory
from .models import Dish
from django.contrib.auth.models import User


class UserDishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'url',
            'name'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    dishes = UserDishSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'dish'
        )


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
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Dish
        fields = (
            'url',
            'name',
            'dish_category',
            'owner',
            'description',
            'ingredients',
            'recipe',
            'post_date',
            'difficulty_1_10',
            'created'

        )

