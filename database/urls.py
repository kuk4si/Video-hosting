
from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('profiles/', include(('profiles.urls', 'profiles'))),
    path('', index, name='index'),
]
