from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request, name: str, num:int):
    return HttpResponse(f"<h1>{num}. {name.title()}, Welcome to django!</h1>")

def index(request):
    name = "Adeshola"
    return render(request, 'index.html', context={"name": name})

