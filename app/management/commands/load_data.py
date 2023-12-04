import json
import os
from django.core.management.base import BaseCommand
from app.models import CarMake, CarModel, CarYear
from drf_Project.settings import BASE_DIR

class Command(BaseCommand):
    help = 'Load data from JSON file to the database'

    def handle(self, *args, **options):
        archivo = os.path.join(BASE_DIR, 'data.json')
        with open(archivo, 'r') as file:
            data = json.load(file)

            for entry in data:
                make, created = CarMake.objects.get_or_create(
                    idmake=entry['idmake'],
                    make=entry['make'],
                    slugmake=entry['slugmake']
                )

                model, created = CarModel.objects.get_or_create(
                    idmodel=entry['idmodel'],
                    make=make,
                    model=entry['model'],
                    slugmodel=entry['slugmodel']
                )

                for year in entry['year']:
                    CarYear.objects.get_or_create(
                        car_make=make,
                        car_model=model,
                        year=year
                    )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
