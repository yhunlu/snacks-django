from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order


def say_hello(request):
    queryset = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))

    return render(request, 'hello.html', {'name': 'yahya', 'results': queryset})