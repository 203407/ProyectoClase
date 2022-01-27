from rest_framework.views import APIView 
from rest_framework.response import Response

#importacion de serealizadores
from primerComponenete.serializers import PrimerTablaSerializer

#importacion de modelos
from primerComponenete.models import PrimerModelo

# Create your views here.

class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer = PrimerTablaSerializer(querySet, many=True , context= {'request':request})
        return Response(serializer.data)