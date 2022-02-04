from django.shortcuts import render

from rest_framework.views import APIView 
from loadImage.serializers import FirstTableSerializer
from loadImage.models import PrimerModelo
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

import json

# Create your views here.

suce = '{ "message":"succes"}'
error = '{ "message":"error"}'


def responser_custom(custom, responseData, stats):
        respuesta =""
        if custom == "succes":
            respuesta = json.loads(suce)
        else:
            respuesta = json.loads(error)
        respuesta.update({'pay_load':responseData})
        respuesta.update({'status':stats}) 
        return respuesta

class FirstViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer = FirstTableSerializer(querySet, many=True , context= {'request':request})
        return Response(responser_custom('succes',serializer.data, status.HTTP_200_OK))