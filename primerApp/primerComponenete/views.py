from msilib.schema import Error
from django.template import context
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

    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Error guardado")