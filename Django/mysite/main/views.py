from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.
def index(response, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
#    return HttpResponse('<h1>%s</h1>' % ls.name)
    return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' %(ls.name, str(item.text)))

# def index(response):
#     return HttpResponse('<h1>Hello world</h1>')
# def v1(response):
#     return HttpResponse('View 1')