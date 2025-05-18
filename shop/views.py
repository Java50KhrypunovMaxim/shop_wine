from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from shop.models import Goods, Wine, Mood
from shop.serializers import (GoodsSerializer, WineSerializer,
                              MoodSerializer)


class GoodsViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class =GoodsSerializer


class WineViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer


class MoodleViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer


class OrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100