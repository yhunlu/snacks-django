from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, F, Func
from store.models import Customer, Product, Order


def say_hello(request):
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Func(F('first_name'), Value(
            ''), F('last_name'), function='CONCAT')
    )

    return render(request, 'hello.html', {'name': 'yahya', 'results': list(queryset)})
