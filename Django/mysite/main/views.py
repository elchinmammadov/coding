from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
# def index(response, name):
    # ls = ToDoList.objects.get(name=name)
    ls = ToDoList.objects.get(id=id)
    if response.method == 'POST':
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid")
    # item = ls.item_set.get(id=1)
    # return HttpResponse('<h1>%s</h1>' % ls.name)
    # return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' % (ls.name, str(item.text)))
    return render(response, 'main/list.html', {"ls": ls}) # to find and show to-do list using its id number 

def home(response):
    return render(response, 'main/home.html', {}) # home page (i.e. landing page)

def create(response): # function to create a new to-do list
    if response.method == 'POST': # if we click submit button, it creates a new to-do list and redirects us to its page
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            return HttpResponseRedirect("/%i" % t.id) # redirects to to-do list page that we've just created using its id number
    else:
        form = CreateNewList() # shows form to create a new to-do list
    return render(response, 'main/create.html', {'form': form}) # create to-do list using a form

# def index(response):
#     return HttpResponse('<h1>Hello world</h1>')
# def v1(response):
#     return HttpResponse('View 1')