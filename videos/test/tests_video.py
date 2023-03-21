from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Categorias, Video
from ..serializers import CategoriaSerializer, VideoSerializer


class CategoriasVideoTest(APITestCase):
    def setUp(self):
        self.list_url_videos = reverse("videos-list")
        self.list_url_categoria = reverse("categorias-list")
        self.client = APIClient()
        self.categoria1 = Categorias.objects.create(titulo="Categoria 1", cor="red")
        self.video1 = Video.objects.create(
            titulo="Video 1",
            descricao="Descricao do video 1",
            url="http://www.google.com",
            categoria_id=self.categoria1,
        )

    def test_requisicao_put_para_criar_categoria(self):
        """Teste para criar uma categoria"""
        data = {"titulo": "Nova categoria", "cor": "blue"}
        response = self.client.post(self.list_url_categoria, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_para_criar_video(self):
        """Teste para criar um video"""
        data = {
            "titulo": "Video 2",
            "descricao": "Descricao do video 2",
            "url": "http://video2.com",
            "categoria_id": self.categoria1.id,
        }
        response = self.client.post(self.list_url_videos, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_get_para_listar_videos(self):
        """Teste para listar videos"""
        response = self.client.get(self.list_url_videos)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_categorias(self):
        """Teste para listar categorias"""
        response = self.client.get(self.list_url_categoria)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_put_para_atualizar_video(self):
        """Teste para atualizar um video"""
        data = {
            "titulo": "Video 1",
            "descricao": "Descricao do video 1",
            "url": "http://www.google.com",
            "categoria_id": self.categoria1.id,
        }
        response = self.client.put(
            reverse("videos-detail", args=[self.video1.id]), format="json", data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
