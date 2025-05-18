from rest_framework import serializers

from shop.models import Goods, Wine, Mood


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ("id", "wine")


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = (
            "id", "name", "wine_type", "color", "country", "price")

    def create(self, validated_data):
        moods = validated_data.pop('moods', [])
        wine = Wine.objects.create(**validated_data)
        wine.moods.set(moods)
        return wine

    def update(self, instance, validated_data):
        moods = validated_data.pop('moods', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if moods is not None:
            instance.moods.set(moods)

        return instance



class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ("id", "name")

