from rest_framework import viewsets
from .serializers import ParcelaSerializer
from core.models import Parcela


class ParcelaViewSet(viewsets.ModelViewSet):
    serializer_class = ParcelaSerializer
    queryset = Parcela.objects.all()
