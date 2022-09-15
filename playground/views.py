from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem


def say_hello(request):
    Collection.objects.filter(id__gt=5).delete()

    return render(request, 'hello.html', {'name': 'yahya', 'results': 'list(queryset)'})
