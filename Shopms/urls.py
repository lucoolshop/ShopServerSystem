from django.urls import path, include
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('',include('mainapp.urls')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
