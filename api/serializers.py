from datetime import date
from rest_framework import serializers
from core.models import Parcela

class ParcelaSerializer(serializers.ModelSerializer):
    prazo_restante = serializers.SerializerMethodField()

    class Meta:
        model = Parcela
        fields = '__all__'

    def get_prazo_restante(self, obj):
        hoje = date.today()
        prazo = (obj.prazo.year - hoje.year) * 12 + obj.prazo.month - hoje.month
        return prazo
