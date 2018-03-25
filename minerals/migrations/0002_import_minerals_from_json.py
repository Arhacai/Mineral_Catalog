import json
import os

from io import open
from django.db import migrations
from mineral_catalog.settings import BASE_DIR
from minerals.models import Mineral

filename = os.path.join(BASE_DIR, 'minerals/migrations/minerals.json')


def import_minerals(apps, schema_name):
    with open(filename, encoding='utf-8') as file:
        minerals = json.load(file)
        for mineral in minerals:
            Mineral.objects.create(
                name=mineral.get('name'),
                image_filename=mineral.get('image filename'),
                image_caption=mineral.get('image caption'),
                category=mineral.get('category'),
                formula=mineral.get('formula'),
                strunz_classification=mineral.get('strunz classification'),
                color=mineral.get('color'),
                crystal_system=mineral.get('crystal system'),
                unit_cell=mineral.get('unit cell'),
                crystal_symmetry=mineral.get('crystal symmetry'),
                cleavage=mineral.get('cleavage'),
                mohs_scale_hardness=mineral.get('mohs scale hardness'),
                luster=mineral.get('luster'),
                streak=mineral.get('streak'),
                diaphaneity=mineral.get('diaphaneity'),
                optical_properties=mineral.get('optical properties'),
                refractive_index=mineral.get('refractive index'),
                crystal_habit=mineral.get('crystal habit'),
                specific_gravity=mineral.get('specific gravity'),
                group=mineral.get('group')
            )


class Migration(migrations.Migration):
    dependencies = [
        ('minerals', '0001_initial')
    ]

    operations = [
        migrations.RunPython(import_minerals)
    ]
