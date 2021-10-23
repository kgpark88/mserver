from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.site.site_header = "Admin"
admin.site.site_title = "AIS Portal"
admin.site.index_title = "Welcome to AIS Portal"

schema_view = get_schema_view(
   openapi.Info(
      title="AIS API",
      default_version='v1',
      description="AIS API",
      contact=openapi.Contact(email="kgpark88@gmail.com"),
   ),
   validators=['flex'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^api(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api$', schema_view.with_ui('swagger', cache_timeout=0), name='api'),
    re_path(r'^redoc$', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
  
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('ocr/', include(('ocr.urls', 'ocr'), namespace='ocr')),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
