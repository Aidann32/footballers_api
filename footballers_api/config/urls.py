from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from apps.footballers.views import FootballerViewSet


schema_view = get_swagger_view(title='Footballers API')

router = DefaultRouter()
router.register('footballers', FootballerViewSet, basename='footballers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view)
]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

