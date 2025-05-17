from rest_framework import serializers

from shop.models import Goods, Wine, Mood, Occasion


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ("id", "wine")


class WineSerializer(serializers.ModelSerializer):
    moods = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Mood.objects.all()
    )
    occasions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Occasion.objects.all()
    )

    class Meta:
        model = Wine
        fields = (
            "id", "name", "wine_type", "color", "country", "producer",
            "occasions", "moods", "price", "description", "price_range"
        )

    def create(self, validated_data):
        moods = validated_data.pop('moods', [])
        occasions = validated_data.pop('occasions', [])
        wine = Wine.objects.create(**validated_data)
        wine.moods.set(moods)
        wine.occasions.set(occasions)
        return wine

    def update(self, instance, validated_data):
        moods = validated_data.pop('moods', None)
        occasions = validated_data.pop('occasions', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if moods is not None:
            instance.moods.set(moods)
        if occasions is not None:
            instance.occasions.set(occasions)

        return instance



class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ("id", "name")


class OccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = ("id", "name")