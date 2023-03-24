from django.contrib import admin
from .models import Video, Categorias


class VideoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descricao", "url")
    list_display_links = ("titulo",)
    list_per_page = 10


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cor")
    list_display_links = ("titulo","cor")
    list_per_page = 10


admin.site.register(Video, VideoAdmin)
admin.site.register(Categorias, CategoriaAdmin)
