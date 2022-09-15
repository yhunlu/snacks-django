from django.shortcuts import render
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem
from django.db import connection

def say_hello(request):
    with connection.cursor() as cursor:
        cursor.execute()
        cursor.callproc('get_customer', [1, 3, 4])

    return render(request, 'hello.html', {'name': 'yahya', 'results': list(queryset)})
