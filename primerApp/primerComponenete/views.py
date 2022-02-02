from asyncio.windows_events import NULL
from msilib.schema import Error
from django.template import context
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status


#importacion de serealizadores
from primerComponenete.serializers import PrimerTablaSerializer

#importacion de modelos
from primerComponenete.models import PrimerModelo


import json

# Create your views here.

suce = '{ "message":"succes"}'
error = '{ "message":"error"}'


def responser_custom(custom, responseData, stats):
        respuesta ={}
        if custom == "succes":
            respuesta = json.loads(suce)
        else:
            respuesta = json.loads(error)
        respuesta.update({'pay_load':responseData})
        respuesta.update({'status':stats}) 
        return respuesta
    

class PrimerViewList(APIView):
        
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer = PrimerTablaSerializer(querySet, many=True , context= {'request':request})
        #print(responser_custom('succes',serializer.data,'good'))    
        #return Response(serializer.data)
        return Response(responser_custom('succes',serializer.data, status.HTTP_200_OK))

    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PrimerViewDetail(APIView):
    
    def get_object(self,pk):
        try:
            return PrimerModelo.objects.get(pk=pk)
        except PrimerModelo.DoesNotExist:
            return 404


    def get(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse,context={"request":request})
            #return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(responser_custom('succes',serializer.data,status.HTTP_200_OK))
        else:            
            #return Response("no encontrado",status=status.HTTP_400_BAD_REQUEST)
            return Response(responser_custom('error',"Id no encontrado",status.HTTP_400_BAD_REQUEST))
    
    def put(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, data=request.data, context={"request":request})
            if serializer.is_valid():                
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("no encontrado",status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, data=request.data, context={"request":request})
            if serializer.is_valid():                
                idResponse.delete()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("no encontrado",status=status.HTTP_400_BAD_REQUEST)