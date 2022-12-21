from rest_framework import serializers 
from .models import Registro
 
 
class RegistroSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Registro
        fields = ('id',
                  'nome',
                  'cargo',
                  'cartao')