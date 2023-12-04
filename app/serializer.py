from rest_framework import serializers
from .models import CarMarca, CarModelo, CarAnio


# Modelos Relacionales
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMarca
        read_only_fields = ('id','slugmarca',)
        fields = '__all__'

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['marca'] = data.pop('make')
    #     data['slug_marca'] = data.pop('slugmake')
    #     return data
    
class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModelo
        read_only_fields = ('id','slugmodelo',)
        fields = ('id','marca', 'modelo','slugmodelo',)

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['id_marca'] = data.pop('make')
    #     data['modelo'] = data.pop('model')
    #     data['slug_modelo'] = data.pop('slugmodel')
    #     return data

class AnioSerializer(serializers.ModelSerializer):
    # car_model = serializers.PrimaryKeyRelatedField(queryset=CarModel.objects.all())
    class Meta:
        model = CarAnio
        fields = ('car_marca','car_modelo','anio')
    

        # extra_kwargs = {
        #     'model': {
        #         'queryset': CarModel.objects.all(),
        #         'limit_choices_to': {'make': models.F('make')}
        #     }
        # }

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['id_marca'] = data.pop('make')
    #     data['id_modelo'] = data.pop('idmodel')
    #     data['año'] = data.pop('year')
    #     return data


# class CarDetailSerializer(serializers.ModelSerializer):
#     car_make = CarMakeSerializer()
#     car_model = CarModelSerializer()
#     car_year = CarYearSerializer()


    

# class CarDetailSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     make = serializers.CharField()
#     slugmake = serializers.SlugField()
#     model = serializers.CharField()
#     slugmodel = serializers.SlugField()
#     year = serializers.IntegerField()

#     def create(self, validated_data):
#         year_data = validated_data.pop('year')
#         model_data = validated_data.pop('model')
#         make_data = validated_data.pop('make')

#         make, _ = CarMake.objects.get_or_create(**make_data)
#         model, _ = CarModel.objects.get_or_create(make=make, **model_data)
#         year, _ = CarYear.objects.get_or_create(car_make=make, car_model=model, **year_data)

#         return {
#             'id': make.id,
#             'make': make.make,
#             'slugmake': make.slugmake,
#             'model': model.model,
#             'slugmodel': model.slugmodel,
#             'year': year.year,
#         }
    
# Modelos JSON
# from rest_framework import serializers

# class YearSerializer(serializers.Serializer):
#     year = serializers.IntegerField()

# class CarSerializer(serializers.Serializer):
#     id = serializers.CharField()
#     make = serializers.CharField()
#     slugmake = serializers.CharField()
#     model = serializers.CharField()
#     slugmodel = serializers.CharField()
#     years = YearSerializer(many=True)
        


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