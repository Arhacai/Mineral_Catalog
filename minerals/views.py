from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from collections import OrderedDict
from random import randint

from .models import Mineral


def rand_mineral():
    rand_pk = randint(1, Mineral.objects.all().count())
    return rand_pk


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {
        'minerals': minerals,
        'rand_pk': rand_mineral()}
    )


def mineral_detail(request, pk):
    mineral = model_to_dict(get_object_or_404(Mineral, pk=pk))

    header = OrderedDict()
    if 'id' in mineral:
        header.update({'id': mineral.pop('id')})
    if 'name' in mineral:
        header.update({'name': mineral.pop('name')})
    if 'image_filename' in mineral:
        header.update({'image_filename': mineral.pop('image_filename')})
    if 'image_caption' in mineral:
        header.update({'image_caption': mineral.pop('image_caption')})

    body = OrderedDict()
    if 'group' in mineral:
        body.update({'group': mineral.pop('group')})
    if 'category' in mineral:
        body.update({'category': mineral.pop('category')})
    if 'formula' in mineral:
        body.update({'formula': mineral.pop('formula')})
    if 'strunz_classification' in mineral:
        body.update({
            'strunz_classification': mineral.pop('strunz_classification')})
    if 'crystal_system' in mineral:
        body.update({'crystal_system': mineral.pop('crystal_system')})
    if 'mohs_scale_hardness' in mineral:
        body.update({
            'mohs_scale_hardness': mineral.pop('mohs_scale_hardness')})

    return render(request, 'minerals/detail.html', {
        'header': header,
        'body': body,
        'mineral': mineral,
        'rand_pk': rand_mineral()
    })
