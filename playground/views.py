from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(last_update__year=2021)

    return render(request, 'hello.html', {'name': 'yahya', 'results': list(queryset)})
