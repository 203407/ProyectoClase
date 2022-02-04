#from dataclasses import fields

from rest_framework import serializers    

#importacion de modelos
from loadImage.models import PrimerModelo

class FirstTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerModelo
        fields = ('__all__')