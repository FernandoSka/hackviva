"""AgenteI URLs."""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from AgenteI import settings

urlpatterns = [
    url(r'^superI/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
