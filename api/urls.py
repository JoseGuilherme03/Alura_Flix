from django.urls import path, include
from rest_framework import routers
from videos.views import VideoViewSet, CategoriaViewSet, CategoriaViewList


router = routers.DefaultRouter()
router.register("videos", VideoViewSet)
router.register("categorias", CategoriaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("categorias/<int:pk>/videos/", CategoriaViewList.as_view()),
]
