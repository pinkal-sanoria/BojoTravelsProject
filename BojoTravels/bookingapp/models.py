from django.db import models

# Create your models here.
class Package(models.Model):
    package_name = models.CharField(max_length=100,null=True,blank=True)
    cover_image = models.ImageField(upload_to='media/images/',null=True,blank=True)
    small_description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    rating_out_of_5 = models.DecimalField(max_digits=2, decimal_places=1,null=True,blank=True)
    days = models.IntegerField(null=True,blank=True)
    about_this = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.package_name