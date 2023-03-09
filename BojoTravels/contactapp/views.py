from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, phone=phone, email=email, message=message)
        contact.save()
        
        
         # send email
        subject = 'New message from your website'
        message = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.DEFAULT_FROM_EMAIL]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(request, 'Your message has been sent!')
        return redirect('contact')

    return render(request, 'contactapp/contact.html')

# def contact(request):
#     return render(request,'contactapp/contact.html')