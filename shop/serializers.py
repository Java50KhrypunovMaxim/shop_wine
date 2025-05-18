from rest_framework import serializers

from shop.models import Goods, Wine, Mood, Glass, Corkscrew, Country, Producer


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ("id", "wine")


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ("id", "name", "wine_type", "color", "country", "price")


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