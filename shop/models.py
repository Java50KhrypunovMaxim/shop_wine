from django.db import models

class WineType(models.TextChoices):
    DRY = 'dry'
    SEMI_DRY = 'semi_dry'
    SEMI_SWEET = 'semi_sweet'
    DESSERT = 'dessert'
    SPARKLING = 'sparkling'


class WineColor(models.TextChoices):
    RED = 'red'
    WHITE = 'white'
    ROSE = 'rose'


class OccasionType(models.TextChoices):
    GIFT = 'gift'
    ROMANTIC_DINNER = 'romantic_dinner'
    CELEBRATION = 'celebration'


class MoodType(models.TextChoices):
    ROMANTIC = 'romantic'
    FESTIVE = 'festive'
    CASUAL = 'casual'


class Occasion(models.Model):
    name = models.CharField(
        max_length=50,
        choices=OccasionType.choices,
        default=OccasionType.ROMANTIC_DINNER,
        unique=True
    )

    def __str__(self):
        return self.get_name_display()


class Mood(models.Model):
    name = models.CharField(
        max_length=50,
        choices=MoodType.choices,
        default=MoodType.FESTIVE,
        unique=True
    )

    def __str__(self):
        return self.get_name_display()


class PriceRange(models.TextChoices):
    BUDGET = 'budget'
    MID_RANGE = 'mid-range'
    PREMIUM = 'premium'


class Wine(models.Model):
    name = models.CharField(max_length=200, null=True)
    wine_type = models.CharField(max_length=20, choices=WineType.choices,
                                 default=WineType.DESSERT)
    color = models.CharField(max_length=20, choices=WineColor.choices,
                             default=WineColor.RED)
    country = models.CharField(max_length=200, null=True, blank=True)
    producer = models.CharField(max_length=200, null=True, blank=True)
    occasions = models.ManyToManyField(Occasion, blank=True)
    moods = models.ManyToManyField(Mood, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_range = models.CharField(max_length=20, choices=PriceRange.choices,
                                   default=PriceRange.BUDGET)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Wine"
        verbose_name_plural = "Wines"

    def __str__(self):
        return f"{self.name} ({self.get_wine_type_display()}, {self.get_color_display()})"


class Goods(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)

    def __str__(self):
        return f"Goods: {self.wine.name}"

