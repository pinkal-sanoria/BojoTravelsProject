from django.shortcuts import render
from bookingapp.models import Package
from .models import Person
from galleryapp.models import Media


# Create your views here.
def index(request):
    packages = Package.objects.all() 
    people = Person.objects.all()
    media = Media.objects.all()
    return render(request,'bojoapp/index.html',{'packages': packages,'people':people,'media': media})

