from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from shop.models import Goods, Wine, Mood, Country, Producer, Glass, Corkscrew
from shop.serializers import (GoodsSerializer, WineSerializer,
                              MoodSerializer, CountrySerializer, ProducerSerializer, GlassSerializer,
                              CorkscrewSerializer)


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


class CountryViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ProducerViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class GlassViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Glass.objects.all()
    serializer_class = GlassSerializer


class CorkscrewViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Corkscrew.objects.all()
    serializer_class = CorkscrewSerializer


class OrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100