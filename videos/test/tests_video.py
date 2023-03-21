from rest_framework.test import APITestCase
from ..models import Video, Categorias
from django.urls import reverse
from rest_framework import status


class VideoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("videos-list")
        self.categoria = Categorias.objects.create(titulo="Livre", cor="teste")
        self.video_1 = Video.objects.create(
            titulo="Teste", descricao="Testando...", url="https://www.google.com/"
        )
        self.video_2 = Video.objects.create(
            titulo="Teste2",
            descricao="Testando mais uma vez",
            url="https://www.google.com/",
        )

    def test_requisicao_get_para_videos(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

