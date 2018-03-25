from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect


def redirect_to_minerals(request):
    return HttpResponseRedirect(reverse('minerals:list'))
