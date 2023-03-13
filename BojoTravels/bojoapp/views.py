from django.shortcuts import render
from bookingapp.models import Package
from .models import Person

# Create your views here.
def index(request):
    packages = Package.objects.all()
    people = Person.objects.all()
    return render(request,'bojoapp/index.html',{'packages': packages,'people':people})

