from django.shortcuts import render
from django.http import HttpResponse

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")

def index(request):
    return render(request, 'home/index.html', context={'dict_data': thisdict})

def contact(request):
    return render(request, 'home/contact.html', )
