from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
# def index(response, name):
    # ls = ToDoList.objects.get(name=name)
    ls = ToDoList.objects.get(id=id)
    # item = ls.item_set.get(id=1)
    # return HttpResponse('<h1>%s</h1>' % ls.name)
    # return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' % (ls.name, str(item.text)))
    return render(response, 'main/list.html', {"ls": ls})

def home(response):
    return render(response, 'main/home.html', {}) # home page (i.e. landing page)

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            return HttpResponseRedirect('/%i' % t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {'form': form}) # create to-do list

# def index(response):
#     return HttpResponse('<h1>Hello world</h1>')
# def v1(response):
#     return HttpResponse('View 1')