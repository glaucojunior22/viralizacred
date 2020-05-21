from django.urls import path, include
from .router import api_urlpatterns

app_name = 'api'

urlpatterns = [
    path('', include(api_urlpatterns))
]