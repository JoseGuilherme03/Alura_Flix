from rest_framework import viewsets
from .serializers import VideoSerializer
from .models import Video


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

