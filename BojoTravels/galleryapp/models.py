from django.db import models

class Media(models.Model):
    image = models.ImageField(upload_to='media/images/',null=True,blank=True)
    image_name = models.CharField(max_length=255,null=True,blank=True)
    video = models.FileField(upload_to='media/video/',null=True,blank=True)
    video_name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.image_name + ' / ' + self.video_name