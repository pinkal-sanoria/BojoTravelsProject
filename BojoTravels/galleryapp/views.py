from django.shortcuts import render
from .models import Media

# Create your views here.
def gallery(request):
    media = Media.objects.all()
    return render(request,'galleryapp/gallery.html',{'media': media})

