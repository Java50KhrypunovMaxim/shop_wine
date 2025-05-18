from django.urls import path, include
from rest_framework import routers
from shop.views import GoodsViewSet, WineViewSet, MoodleViewSet, CountryViewSet, ProducerViewSet, GlassViewSet, \
    CorkscrewViewSet

app_name = "shop"

router = routers.DefaultRouter()
router.register("goods", GoodsViewSet)
router.register("wine", WineViewSet)
router.register("mood", MoodleViewSet)
router.register("country", CountryViewSet)
router.register("producer", ProducerViewSet)
router.register("glass", GlassViewSet)
router.register("corkscrew", CorkscrewViewSet)


urlpatterns = [path("", include(router.urls))]

