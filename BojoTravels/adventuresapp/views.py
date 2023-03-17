from django.shortcuts import render
from bookingapp.models import Package
# Create your views here.
def adventures(request):
    packages = Package.objects.all() 
    return render(request,'adventuresapp/adventures.html',{'packages':packages})