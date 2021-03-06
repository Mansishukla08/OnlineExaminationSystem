from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Admin
from.serializers import Adminserializer
class Adminview(viewsets.ModelViewSet):
    queryset=Admin.objects.all()
    serializer_class=Adminserializer

# Create your views here.
class Adminbyname(APIView):
    def get(self,request,name):
        Admins=Admin.objects.get(username=name)
        serializer=Admin
        return Response(serializer.data)
      
class Categoryview(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=Categoryserializer
    
class Categorybyname(APIView):
    def get(self,request,name):
        categories=Category.objects.get(category_name=name)
        serializer=Categoryserializer(categories)
        return Response(serializer.data)
      
