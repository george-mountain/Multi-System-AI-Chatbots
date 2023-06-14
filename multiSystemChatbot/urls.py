from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    # User management
    path("accounts/", include("allauth.urls")),
    path("apps/", include("chatbots.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
