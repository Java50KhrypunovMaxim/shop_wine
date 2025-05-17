from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from shop.models import Goods, Wine, Mood, Occasion
from shop.serializers import GoodsSerializer, WineSerializer, MoodSerializer, OccasionSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class =GoodsSerializer


class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer


class MoodleViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer


class OccasionViewSet(viewsets.ModelViewSet):
    queryset = Occasion.objects.all()
    serializer_class = OccasionSerializer


class OrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100