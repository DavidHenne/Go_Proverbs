from django.http import Http404
from django.shortcuts import render

from .models import Proverb

import random


def index(request):
    proverbs = Proverb.objects.all()
    return render(request,
                  'proverbs/index.html',
                  {'proverbs': proverbs})

def detail(request, proverb_id):
    try:
        proverb = Proverb.objects.get(pk=proverb_id)
    except Proverb.DoesNotExist:
        raise Http404(f'No proverb available for id {proverb_id}')
    return render(request,
                  'proverbs/detail.html',
                  {'proverb': proverb})

def random_proverb(request):
    pks = [p.id for p in Proverb.objects.all()]
    rand_id = random.choice(pks)
    proverb = Proverb.objects.get(pk=rand_id)
    return render(request,
                  'proverbs/detail.html',
                  {'proverb': proverb})
