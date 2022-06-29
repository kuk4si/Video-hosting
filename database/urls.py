from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('profiles/', include(('profiles.urls', 'profiles'))),
    path('', include(('videos.urls', 'videos'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
