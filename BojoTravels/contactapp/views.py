from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        category = request.POST.get('category')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        date = request.POST.get('date')
        message = request.POST.get('message')

        contact = Contact(name=name,
            email=email,
            contact_number=contact_number,
            category=category,
            adults=adults,
            children=children,
            date=date,
            message=message)
        contact.save()
        
        
         # send email
        subject = 'New message from your website'
        message = f'Name: {name}\nPhone: {contact_number}\nEmail: {email}\nMessage: {message}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.DEFAULT_FROM_EMAIL]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(request, 'Your message has been sent!')
        print('Your email has been sent!')
        return redirect('contact')

    return render(request, 'contactapp/contact.html')

