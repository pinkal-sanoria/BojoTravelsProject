from django.shortcuts import render,get_object_or_404
from .models import Package
# Create your views here.

def booking(request):
    package_id = request.GET.get('package_id')
    package = get_object_or_404(Package, id=package_id)
    return render(request,'bookingapp/booking.html', {'package': package})
