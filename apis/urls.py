from django.urls import path, include
from . import views
from .views import CMCView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = "apis"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/cmc', CMCView.as_view()),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)