from django.shortcuts import render,get_object_or_404
from .models import Package
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from contactapp.models import TourBooking
from bookingapp.models import Package
# Create your views here.

def booking(request):
    packages = Package.objects.all()
    package_id = request.GET.get('package_id')
    package = get_object_or_404(Package, id=package_id)
    
    if request.method == 'POST':
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        tour_rate = request.POST.get('tour_rate')
        date = request.POST.get('date')

        tour_booking = TourBooking(
            adults=adults,
            children=children,
            contact_number=contact_number,
            email=email,
            tour_rate=tour_rate,
            date=date
        )
        tour_booking.save()
        subject = 'New message from your website'
        message = f'Name:{tour_rate} \nPhone: {contact_number}\nEmail: {email}\nMessage: {tour_rate}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.DEFAULT_FROM_EMAIL]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        messages.success(request, 'Your tour booking has been submitted!')
        # return redirect(request,'bookingapp/booking.html', {'package': package})
    
    
    return render(request,'bookingapp/booking.html', {'package': package,'packages':packages})


