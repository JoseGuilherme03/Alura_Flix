from django.urls import path, include
from rest_framework import routers
from videos.views import (
    VideoViewSet,
    CategoriaViewSet,
    CategoriaViewList,
    VideosFreeViewList,
)


router = routers.DefaultRouter()
router.register("videos", VideoViewSet, basename="videos")
router.register("categorias", CategoriaViewSet, basename="categorias")

urlpatterns = [
    path("videos/free/", VideosFreeViewList.as_view()),
    path("", include(router.urls)),
    path("categorias/<int:pk>/videos/", CategoriaViewList.as_view()),
]
