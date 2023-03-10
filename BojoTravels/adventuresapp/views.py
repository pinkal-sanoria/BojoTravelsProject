from django.shortcuts import render

# Create your views here.
def adventures(request):
    return render(request,'adventuresapp/adventures.html')