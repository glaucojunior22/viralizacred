from rest_framework import routers
from .views import ParcelaViewSet

router = routers.DefaultRouter()

router.register(r'parcelas', ParcelaViewSet)

api_urlpatterns = router.urls