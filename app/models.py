from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core import validators
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# class Car(models.Model):
#     brand = models.CharField()
#     model = models.CharField()
#     year = models.PositiveIntegerField()

class CarMarca(models.Model):
    marca = models.CharField(max_length=255, unique=True, verbose_name="Marca")
    slugmarca = models.SlugField(unique=True, verbose_name="Slug Marca", blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slugmarca:
            self.slugmarca = slugify(self.marca)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.marca
    
class CarModelo(models.Model):
    marca = models.ForeignKey(CarMarca, on_delete=models.CASCADE, verbose_name="Id Marca")
    # idmodel = models.IntegerField(unique=True, verbose_name="Id Modelo")
    modelo = models.CharField(max_length=255, unique=True, verbose_name="Modelo")
    slugmodelo = models.SlugField(unique=True, verbose_name="Slug Modelo", blank=True)

    def save(self, *args, **kwargs):
        if not self.slugmodelo:
            self.slugmodelo = slugify(self.modelo)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.modelo


def validate_year(value):
    current_year = timezone.now().year
    if value > current_year:
        raise ValidationError(f'El año no puede ser mayor al año actual ({current_year}).')
    
class CarAnio(models.Model):
    car_marca = models.ForeignKey(CarMarca, on_delete=models.CASCADE, verbose_name="Id Marca")
    car_modelo = models.ForeignKey(CarModelo, on_delete=models.CASCADE, verbose_name="Id Modelo") #, limit_choices_to={'make__id': models.F('make')}
    anio = models.IntegerField(max_length=4,verbose_name="Año",
                               validators=[validate_year, 
                                           MinValueValidator(1900), 
                                           MaxValueValidator(limit_value=9999)],
                            )
    
    
    def limit_car_models(self):
        return CarModelo.objects.filter(make=self.car_marca)

    class Meta:
        unique_together = ['car_marca', 'car_modelo', 'anio']

    
    def __str__(self) -> str:
        return self.year


@receiver(pre_save, sender=CarMarca)
def capitalize_marca_nombre(sender, instance, **kwargs):
    instance.marca = instance.marca.capitalize()

@receiver(pre_save, sender=CarModelo)
def capitalize_modelo_nombre(sender, instance, **kwargs):
    instance.modelo = instance.modelo.capitalize()