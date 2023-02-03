from .views import IndexView
from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
