from rest_framework import serializers
from .models import Carreras

class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        
        fields = ('nombre','clave','plan_estudios','is_active')