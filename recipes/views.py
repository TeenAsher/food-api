from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Dish
from .models import DishCategory
from .serializers import DishSerializer
from .serializers import DishCategorySerializer
from rest_framework import permissions
from .custompermission import IsCurrentUserOwnerOrReadOnly
from rest_framework.throttling import ScopedRateThrottle


class DishCategoryList(generics.ListCreateAPIView):
    throttle_scope = 'dish-categories'
    throttle_classes = (ScopedRateThrottle,)
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    name = 'dishcategory-list'


class DishCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'dish-categories'
    throttle_classes = (ScopedRateThrottle,)
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    name = 'dishcategory-detail'


class DishList(generics.ListCreateAPIView):
    throttle_scope = 'dishes'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    name = 'dish-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'dishes'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    name = 'dish-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'dish-categories': reverse(DishCategoryList.name, request=request),
            'dishes': reverse(DishList.name, request=request)
        })