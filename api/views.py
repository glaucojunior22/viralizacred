from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ParcelaSerializer
from core.models import Parcela


class ParcelaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ParcelaSerializer
    queryset = Parcela.objects.all()
    permission_classes = [IsAuthenticated]
