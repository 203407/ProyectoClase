from rest_framework.views import APIView 
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import FirstSerializerRegister
import json
from rest_framework import status

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
       

class RegisterView(APIView):
    
    # get para corroborar que se creo el usuario
    def get(self, request, format=None):
        querySet = User.objects.all()
        serializer = FirstSerializerRegister(querySet, many=True , context= {'request':request})        
        return Response(responser_custom('succes',serializer.data, status.HTTP_200_OK))
    
    def post(self, request, format=None):       
        serializer= FirstSerializerRegister(data=request.data, context={'request':request})
        
        if serializer.is_valid():
            datos = request.data               
            username = str(datos.__getitem__('username'))
            email = str(datos.__getitem__('email'))
            password = str(datos.__getitem__('password'))            
                        
            user = User(
            username = username,
            email = email
            )
    
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()    

            return Response(responser_custom('succes',"Usuario creado",status.HTTP_201_CREATED))
        else:
            return Response(responser_custom('error',serializer.errors,status.HTTP_400_BAD_REQUEST))
