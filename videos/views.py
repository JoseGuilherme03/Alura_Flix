from rest_framework import viewsets, generics
from .serializers import VideoSerializer, CategoriaSerializer
from .models import Video, Categorias
from rest_framework import filters


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "titulo",
    ]


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categorias.objects.all()


class CategoriaViewList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset

    serializer_class = VideoSerializer
