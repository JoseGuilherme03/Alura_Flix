from django.db import models


class Categorias(models.Model):
    titulo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    url = models.CharField(max_length=2048)
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo