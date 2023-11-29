from rest_framework import serializers
# from .models import Car

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         # fields = ('id','brand','model','year',)
#         model = Car
#         fields = '__all__'


# Modelos CSV

# class AnioSerializer(serializers.Serializer):
#     anio = serializers.IntegerField()


# class ModeloSerializer(serializers.Serializer):
#     slugmodelo = serializers.SlugField()
#     modelo = serializers.CharField()
#     anios = AnioSerializer(many=True)

# class MarcaSerializer(serializers.Serializer):
#     slugmarca = serializers.SlugField()
#     marca = serializers.CharField()
#     models = ModeloSerializer(many=True)


# Modelos JSON
from rest_framework import serializers

class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField()

class CarSerializer(serializers.Serializer):
    id = serializers.CharField()
    make = serializers.CharField()
    slugmake = serializers.CharField()
    model = serializers.CharField()
    slugmodel = serializers.CharField()
    years = YearSerializer(many=True)
        