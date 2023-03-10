from django.shortcuts import render
from bookingapp.models import Package
# Create your views here.
def index(request):
    packages = Package.objects.all()
    return render(request,'bojoapp/index.html',{'packages': packages})

