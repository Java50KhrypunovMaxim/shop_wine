from django.db import models


class WineColor(models.TextChoices):
    RED = 'red'
    WHITE = 'white'
    ROSE = 'rose'


class MoodType(models.TextChoices):
    ROMANTIC = 'romantic'
    FESTIVE = 'festive'
    CASUAL = 'casual'


class PriceRange(models.TextChoices):
    BUDGET = 'budget'
    MID_RANGE = 'mid-range'
    PREMIUM = 'premium'


class MaterialForGlasses(models.TextChoices):
    GLASS = 'glass'
    CRYSTAL = 'crystal'
    PLASTIC = 'plastic'


class MaterialForCorkscrew(models.TextChoices):
    WOOD = 'wood'
    STAINLESS = 'stainless steel'
    STEEL = 'steel'


class WineType(models.TextChoices):
    DRY = 'dry'
    SEMI_DRY = 'semi_dry'
    SEMI_SWEET = 'semi_sweet'
    DESSERT = 'dessert'
    SPARKLING = 'sparkling'


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name_of_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name_of_region = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name_of_region or 'Unknown region'} of {self.name_of_country}"


class Mood(models.Model):
    name = models.CharField(
        max_length=50,
        choices=MoodType.choices,
        default=MoodType.FESTIVE,
    )

    def __str__(self):
        return self.get_name_display()


class Wine(models.Model):
    name = models.CharField(max_length=200, null=True)
    wine_type = models.CharField(
        max_length=20,
        choices=WineType.choices,
        default=WineType.DESSERT,
    )
    color = models.CharField(
        max_length=20,
        choices=WineColor.choices,
        default=WineColor.RED,
    )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=False)
    vintage_year = models.IntegerField(null=True)
    alcohol = models.DecimalField(max_digits=4, decimal_places=1, null=True)  # e.g., 13.5%
    moods = models.ManyToManyField(Mood, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_range = models.CharField(
        max_length=20,
        choices=PriceRange.choices,
        default=PriceRange.BUDGET,
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Wine"
        verbose_name_plural = "Wines"

    def __str__(self):
        return f"{self.name} ({self.get_wine_type_display()}, {self.get_color_display()})"


class Glass(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    diameter = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    material = models.CharField(
        max_length=50,
        choices=MaterialForGlasses.choices,
        default=MaterialForGlasses.GLASS,
    )

    def __str__(self):
        return f"{self.name} ({self.capacity}ml)"


class Corkscrew(models.Model):
    name = models.CharField(max_length=200, null=True)
    dimensions = models.CharField(max_length=200, null=True)
    material = models.CharField(
        max_length=50,
        choices=MaterialForCorkscrew.choices,
        default=MaterialForCorkscrew.STAINLESS,
    )

    def __str__(self):
        return f"{self.name} ({self.dimensions})"


class Goods(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    glass = models.ForeignKey(Glass, on_delete=models.CASCADE)
    corkscrew = models.ForeignKey(Corkscrew, on_delete=models.CASCADE)

    def __str__(self):
        return f"Goods: {self.wine.name}, {self.glass.name if self.glass else 'No Glass'}, {self.corkscrew.name if self.corkscrew else 'No Corkscrew'}"

