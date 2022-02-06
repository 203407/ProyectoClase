#from dataclasses import fields

from dataclasses import fields
from rest_framework import serializers    

#importacion de modelos
from loadImage.models import ImgTableModel

class FirstTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgTableModel
        fields = ('__all__')
