from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user/', include('user.urls')),
    path('movie/', include('movie.urls')),
    path('game/', include('game.urls')),
    path('music/', include('music.urls')),
]

handler404 = "home.views.handler404"

if settings.DEBUG:
     from django.conf.urls.static import static
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

