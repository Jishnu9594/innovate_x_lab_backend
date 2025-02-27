from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include("local_apps.main.urls")),
    path("innovatex/", include("local_apps.innovatex.urls")),
    path("message_uitility/", include("local_apps.message_uitility.urls")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
