from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descricao", "url")
    list_display_links = ("titulo",)
    list_per_page = 10


admin.site.register(Video, VideoAdmin)
