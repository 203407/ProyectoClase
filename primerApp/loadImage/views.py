from django.shortcuts import render

# Create your views here.
from posixpath import split
from unicodedata import name
from django.http import QueryDict
from django.shortcuts import render

from rest_framework.views import APIView 
from loadImage.serializers import FirstTableSerializer
from loadImage.models import ImgTableModel
from rest_framework.response import Response
from rest_framework import status
from loadImage.serializers import FirstTableSerializer

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
        querySet = ImgTableModel.objects.all()
        serializer = FirstTableSerializer(querySet, many=True , context= {'request':request})
        return Response(responser_custom('succes',serializer.data, status.HTTP_200_OK))

    def post(self, request, format=None):        
        serializer = FirstTableSerializer(data=request.data, context={"request":request})                                
        if serializer.is_valid():                        
            datos = request.data
            nameImg = str(datos.__getitem__('url_img')).split(".")
            datos.__setitem__('name_img',nameImg[0])
            datos.__setitem__('format_img',nameImg[1])
            serializer2 = FirstTableSerializer(data=datos, context={"request":request})   
            if serializer2.is_valid():                                         
                serializer2.save()                
            return Response(responser_custom('succes',serializer2.data, status.HTTP_201_CREATED))
        else:        
            return Response(responser_custom('error',serializer.errors, status.HTTP_400_BAD_REQUEST))


class FirstViewDetail(APIView):
    
    def get_object(self,pk):
        try:
            return ImgTableModel.objects.get(pk=pk)
        except ImgTableModel.DoesNotExist:
            return 404

    def get(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = FirstTableSerializer(idResponse,context={"request":request})            
            return Response(responser_custom('succes',serializer.data,status.HTTP_200_OK))
        else:                        
            return Response(responser_custom('error',"Id no encontrado",status.HTTP_400_BAD_REQUEST))
   
    def put(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = FirstTableSerializer(idResponse, data=request.data, context={"request":request})            
            if serializer.is_valid():                
                datos = request.data
                nameImg = str(datos.__getitem__('url_img')).split(".")
                datos.__setitem__('name_img',nameImg[0])
                datos.__setitem__('format_img',nameImg[1])
                serializer2 = FirstTableSerializer(idResponse, data=datos, context={"request":request})   
                if serializer2.is_valid():                               
                    serializer2.save()                                     
                return Response(responser_custom('succes',serializer2.data,status.HTTP_200_OK))
            else:                
                return Response(responser_custom('error',serializer.errors,status.HTTP_400_BAD_REQUEST))
        else:            
            return Response(responser_custom('error',"Id no encontrado",status.HTTP_400_BAD_REQUEST))
    
    def delete(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = FirstTableSerializer(idResponse, data=request.data, context={"request":request})
            if serializer.is_valid():                
                idResponse.delete()                
                return Response(responser_custom('succes',serializer.data,status.HTTP_200_OK))
            else:                
                return Response(responser_custom('error',serializer.errors,status.HTTP_400_BAD_REQUEST))
        else:            
            return Response(responser_custom('error',"Id no encontrado",status.HTTP_400_BAD_REQUEST)) 