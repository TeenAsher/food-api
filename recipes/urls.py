from django.urls import path
from .views import DishCategoryList
from .views import DishCategoryDetail
from .views import DishList
from .views import DishDetail
from .views import ApiRoot


urlpatterns = [
    path('dish-categories/', DishCategoryList.as_view(), name=DishCategoryList.name),
    path('dish-categories/<int:pk>', DishCategoryDetail.as_view(), name=DishCategoryDetail.name),
    path('dishes/', DishList.as_view(), name=DishList.name),
    path('dishes/<int:pk>', DishDetail.as_view(), name=DishDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name)
]

