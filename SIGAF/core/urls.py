from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_usuario.urls')),
    path('facilitis/', include('app_facilitis.urls')),
    path('atletas/', include('app_atleta.urls'))
]