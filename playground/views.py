from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    # related fields and inner join
    # queryset = Product.objects.values('id', 'title', 'collection__title')
    queryset = Product.objects.values_list('id', 'title', 'collection__title')

    return render(request, 'hello.html', {'name': 'yahya', 'results': list(queryset)})
