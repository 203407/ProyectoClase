from urllib import request
from rest_framework.views import APIView 
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import FirstSerializerRegister
import json
from rest_framework import status
from rest_framework.permissions import AllowAny


from django.contrib.auth.models import User
from .serializers import RegisterSerializer,ProfileSerializerRegister,RegisterSerializer2
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Profile



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
    permission_classes = (AllowAny,)
    
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
   

   
class RegisterIdView(APIView):
    permission_classes = (AllowAny,)

    def get_objectU(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return 404  
    
    def get_objectP(self,pk):
        try:
            return Profile.objects.get(user=pk)
        except Profile.DoesNotExist:
            return 404  
     

    def get(self,request,pk,format=None):
        idResponse = self.get_objectU(pk)

        if idResponse != 404:

            serializer = RegisterSerializer(idResponse,context={"request":request})    
            idResponseP = self.get_objectP(pk) 

            if idResponseP != 404:                
                serializerP = ProfileSerializerRegister(idResponseP,context={"request":request})    
                respuesta = json.dumps(serializer.data)
                respuesta = json.loads(respuesta)

                respuesta2 = json.dumps(serializerP.data)
                respuesta2 = json.loads(respuesta2)
                respuesta.update(respuesta2)
                
                return Response(respuesta)
            else:                                 
                respuesta = json.dumps(serializer.data)                
                respuesta = json.loads(respuesta)
                respuesta.update( {"user":0,"img_profile":0})
                return Response(respuesta)

        else:                        
            return Response(status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk,format=None):
        idResponse = self.get_objectU(pk)        
        idResponseP = self.get_objectP(pk)
        
        if idResponse != 404:                        
            user = RegisterSerializer2(idResponse,data=request.data, context={"request":request})            
            serializerP = ProfileSerializerRegister(data=request.data, context={"request":request})

            if user.is_valid() and serializerP.is_valid():                
                                
                lost = user.save()       
                prof = serializerP.save()

                print(serializerP.data)
                if prof.user != None:                        
                    return Response(status.HTTP_200_OK)
                else:
                    prof.user = lost 
                    prof.save()
                    return Response(status.HTTP_200_OK)
                                                                                      
            else:                
                return Response(user.errors,status.HTTP_400_BAD_REQUEST)
        else:            
            return Response("Id no encontrado",status.HTTP_400_BAD_REQUEST)
            
class RegisterViewNew(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



    
       
   

   