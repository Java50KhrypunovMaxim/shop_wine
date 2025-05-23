from rest_framework import serializers

from shop.models import Wine, Mood, Glass, Corkscrew, Country, Producer, Order, Product


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "nameOfProduct", "type", "price")


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ("id", "name", "wine_type", "color", "country")


class GlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glass
        fields = ("id", "name")


class CorkscrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corkscrew
        fields = ("id", "name")


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ("id", "name")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ("id", "name_of_country", "name_of_region")


class OrderSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "user", "products")