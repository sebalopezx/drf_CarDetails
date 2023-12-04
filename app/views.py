# from rest_framework.response import Response
# from rest_framework.views import APIView
# import pandas as pd
# from django.shortcuts import render
# from rest_framework import viewsets, generics
# # from .serializer import MarcaSerializer, ModeloSerializer, AnioSerializer
# import json
# import os
# from rest_framework import status
# from .serializer import CarMakeSerializer, CarModelSerializer, CarYearSerializer
# from .models import CarMake, CarModel, CarYear





# Clases con JSON
# class CarView(APIView):
#     def get(self, request, format=None):
#         # Lee el archivo JSON y carga los datos
#         with open('data.json', 'r') as json_file:
#             cars_data = json.load(json_file)

#         # Serializa los datos y los devuelve como respuesta
#         serializer = CarSerializer(cars_data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

# class CarView(APIView):
#     def get(self, request, *args, **kwargs):
#         # Cargar datos desde el JSON
#         json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')
        
#         with open(json_path) as json_file:
#             data = json.load(json_file)

#         # Retorna la respuesta
#         return Response(data)
     

# Clases de CSV

# class MarcaView(APIView):
#     def get(self, request, format=None):
#         marcas_df = pd.read_csv('marcas.csv')
#         serializer = MarcaSerializer(marcas_df, many=True)
#         return Response(serializer.data)
#     @staticmethod
#     def get_extra_actions():
#         return []
        
# class ModeloView(APIView):
#     def get(self, request, marca_slug, format=None):
#         modelos_df = pd.read_csv('modelos.csv')
#         # modelos = modelos_df[modelos_df['make']['slug'] == marca_slug].to_dict(orient='records')
#         modelos = modelos_df[modelos_df['fkmake'] == marca_slug].to_dict(orient='records')
#         serializer = ModeloSerializer(modelos, many=True)
#         return Response(serializer.data)
#     @staticmethod
#     def get_extra_actions():
#         return []
    
# class AnioView(APIView):
#     def get(self, request, modelo_slug, format=None):
#         anios_df = pd.read_csv('anios.csv')
#         # anios = anios_df[anios_df['model']['slug'] == modelo_slug].to_dict(orient='records')
#         anios = anios_df[anios_df['fkmodel'] == modelo_slug].to_dict(orient='records')
#         serializer = AnioSerializer(anios, many=True)
#         return Response(serializer.data)
#     @staticmethod
#     def get_extra_actions():
#         return []
    

