from datetime import date
from rest_framework import serializers
from core.models import Parcela

class ParcelaSerializer(serializers.ModelSerializer):
    prazo_restante = serializers.SerializerMethodField()
    valor_restante = serializers.SerializerMethodField()

    class Meta:
        model = Parcela
        fields = '__all__'

    def get_prazo_restante(self, obj):
        hoje = date.today()
        prazo = (obj.prazo.year - hoje.year) * 12 + obj.prazo.month - hoje.month
        if prazo < 0:
            prazo = 0
        return prazo

    def get_valor_restante(self, obj):
        return float(obj.valor * self.get_prazo_restante(obj))
