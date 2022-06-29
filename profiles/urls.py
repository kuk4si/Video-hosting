
from .views import ProfileDetail
from django.urls import path


urlpatterns = [
    path('profile/<int:pk>', ProfileDetail.as_view(), name='detail')
]
