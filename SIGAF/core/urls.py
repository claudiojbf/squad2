from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_usuario.urls')),
    path('facilitis/', include('app_facilitis.urls')),
    path('atletas/', include('app_atleta.urls')),
    path('funcionarios/', include('app_funcionario.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)