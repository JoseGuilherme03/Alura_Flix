from rest_framework import viewsets, generics
from .serializers import VideoSerializer, CategoriaSerializer
from .models import Video, Categorias


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categorias.objects.all()


class CategoriaViewList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset

    serializer_class = VideoSerializer
