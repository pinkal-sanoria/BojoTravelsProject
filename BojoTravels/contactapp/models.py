# from django.db import models

# # Create your models here.
# class Contact(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255,null=True,blank=True)
#     phone = models.CharField(max_length=20,null=True,blank=True)
#     email = models.EmailField(max_length=255,null=True,blank=True)
#     message = models.TextField(null=True,blank=True)

#     def __str__(self):
#         return self.name
   
   
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100 ,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=15,null=True, blank=True)
    category = models.CharField(max_length=50,null=True, blank=True)
    adults = models.IntegerField(default=0, null=True)
    children = models.IntegerField(default=0,null=True)
    date = models.DateField(null=True,default='', blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
   
   
class TourBooking(models.Model):
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    tour_rate = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f'{self.tour_rate} Tour Booking for {self.date}'