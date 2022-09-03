from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, F
from store.models import Customer, Product, Order


def say_hello(request):
    queryset = Customer.objects.annotate(new_id=F('id') + 1)

    return render(request, 'hello.html', {'name': 'yahya', 'results': list(queryset)})
