from urllib import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import UserAccount

from .serializer import UserDetails, UserRegister
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserRegisterView(generics.ListCreateAPIView):
    serializer_class=UserRegister
    queryset=UserAccount.objects.all()
    filter_backends=[OrderingFilter,SearchFilter]
    search_fields=['first_name','last_name']

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({"user":UserRegister(user,context=self.get_serializer_context()).data,
        "message":"Registered successfully"},status=status.HTTP_201_CREATED)


class UserDetailsView(APIView):
    
    def get(self,request,pk):

        user=UserAccount.objects.get(pk=pk)
        serializer=UserDetails(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        user=UserAccount.objects.get(pk=pk)
        serializer=UserDetails(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User data updated successfullly'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        user=UserAccount.objects.get(pk=pk)
        user.delete()
        return Response({"message":"Deleted successfully"},status=status.HTTP_200_OK)
