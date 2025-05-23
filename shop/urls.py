from django.urls import path, include
from rest_framework import routers
from shop.views import ProductViewSet, WineViewSet, MoodleViewSet, CountryViewSet, ProducerViewSet, GlassViewSet, \
    CorkscrewViewSet, OrderViewSet

app_name = "shop"

router = routers.DefaultRouter()
router.register("products",ProductViewSet)
router.register("wine", WineViewSet)
router.register("mood", MoodleViewSet)
router.register("country", CountryViewSet)
router.register("producer", ProducerViewSet)
router.register("glass", GlassViewSet)
router.register("corkscrew", CorkscrewViewSet)
router.register("order", OrderViewSet)


urlpatterns = [path("", include(router.urls))]

