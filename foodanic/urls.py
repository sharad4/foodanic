from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('markdownx', include('markdownx.urls')),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('u/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)
