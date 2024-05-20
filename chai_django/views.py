# Views for chai_django project
from django.http import HttpResponse
from django.shortcuts import render

# Return Normal Text Response
# def home(request):
#     return HttpResponse("Welcome HomaPage")

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")