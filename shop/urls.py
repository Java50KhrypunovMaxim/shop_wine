from django.urls import path, include
from rest_framework import routers
from shop.views import GoodsViewSet, WineViewSet, MoodleViewSet

app_name = "shop"

router = routers.DefaultRouter()
router.register("goods", GoodsViewSet)
router.register("wine", WineViewSet)
router.register("mood", MoodleViewSet)

urlpatterns = [path("", include(router.urls))]

