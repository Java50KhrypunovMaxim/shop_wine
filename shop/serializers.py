from rest_framework import serializers

from shop.models import Goods, Wine, Mood, Occasion


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ("id", "wine")


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ("id", "name", "wine_type",
                  "color", "country", "producer",
                  "occasions", "moods", "price",
                  "description", "price_range")


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ("id", "name")


class OccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = ("id", "name")