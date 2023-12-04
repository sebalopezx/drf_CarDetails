from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
# from .serializer import MarcaSerializer, ModeloSerializer, AnioSerializer
import json
import os
from rest_framework import status
from .serializer import MarcaSerializer, ModeloSerializer, AnioSerializer
from .models import CarMarca, CarModelo, CarAnio



class MarcaView(viewsets.ModelViewSet):
    queryset = CarMarca.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MarcaSerializer

class ModeloView(viewsets.ModelViewSet):
    queryset = CarModelo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ModeloSerializer

class AnioView(viewsets.ModelViewSet):
    queryset = CarAnio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AnioSerializer


# class CarDetailView(viewsets.ModelViewSet):
#     queryset = CarYear.objects.all()

#     def get_serializer_class(self):
#         return CarYearSerializer


# class CarMakeView(generics.ListCreateAPIView):
#     queryset = CarMake.objects.all()
#     serializer_class = CarMakeSerializer

# class CarModelView(generics.ListCreateAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarModelSerializer

# class CarYearView(generics.ListCreateAPIView):
#     queryset = CarYear.objects.all()
#     serializer_class = CarYearSerializer



# class CarView(APIView):
#     def get(self, request, *args, **kwargs):
#         # Cargar datos desde el JSON
#         json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')
        
#         with open(json_path) as json_file:
#             data = json.load(json_file)

#         # Retorna la respuesta
#         return Response(data)