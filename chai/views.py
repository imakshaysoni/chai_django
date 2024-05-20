from django.shortcuts import render

# Create your views here.
def chai_app(request):
    return render(request, "chai/chai.html")