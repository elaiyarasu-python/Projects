from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate
from .serializers import *


class UserView(APIView):

    def post(self,request):

        new_user = User(username = request.data['username'],is_superuser = request.data['is_superuser'])

        new_user.set_password(request.data['password'])

        new_user.save()

        return Response('new user created')
    

class UserLoginView(APIView):


    #def post(self , request):

      #  user_verification = authenticate(username = request.data['username'],password = request.data['password'])

       # print(user_verification)

        #if user_verification == None:

         #   return Response("login failed")
        
        #else :

         #   return Response("valid user")


     def post(self, request):

        user_data = CustomToken_serializer(data=request.data)

        if user_data.is_valid():
           return Response(user_data.validated_data)
        else:
           return Response(user_data.errors)


 
