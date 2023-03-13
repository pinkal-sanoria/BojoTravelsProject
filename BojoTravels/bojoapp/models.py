from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    reviews = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name