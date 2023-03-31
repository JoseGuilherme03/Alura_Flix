from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Alura FLix",
        default_version="v1",
        description="Provedora de videos, series e filmes",
        terms_of_service="#",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="doc_api",
    ),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
