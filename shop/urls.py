from django.urls import path, include
from rest_framework import routers
from shop.views import GoodsViewSet, WineViewSet, MoodleViewSet, OccasionViewSet

app_name = "shop"

router = routers.DefaultRouter()
router.register("goods", GoodsViewSet)
router.register("wine", WineViewSet)
router.register("mood", MoodleViewSet)
router.register("occasion", OccasionViewSet)

urlpatterns = [path("", include(router.urls))]

