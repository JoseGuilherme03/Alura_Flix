from rest_framework import serializers
from .models import Video, Categorias
from django.core.validators import URLValidator


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

    def validate_url(self, url):
        val = URLValidator()
        try:
            val(url)
        except:
            raise serializers.ValidationError("URL inválida, informe uma URL válida.")
        return url


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"
