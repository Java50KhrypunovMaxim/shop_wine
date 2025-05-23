from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from shop.models import Product, Wine, Mood, Country, Producer, Glass, Corkscrew, Order
from shop.serializers import (ProductsSerializer, WineSerializer,
                              MoodSerializer, CountrySerializer,
                              ProducerSerializer, GlassSerializer,
                              CorkscrewSerializer, OrderSerializer)


class ProductViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


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

class OrderViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100