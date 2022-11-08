from django.db import models
from datetime import datetime

# Create your models here.
class HeadCard(models.Model):
    photo = models.ImageField(upload_to='media/homecard/%Y')
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Card(models.Model):
    photo = models.ImageField(upload_to='media/card/%Y')
    desc = models.TextField()

    def __str__(self):
        return self.desc

class Emergency(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    button_text= models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class About(models.Model):
    photo = models.ImageField(upload_to='media/homecard/%Y')
    title = models.CharField(max_length=255)
    desc = models.TextField()
    updated = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Services(models.Model):
    photo = models.ImageField(upload_to='media/services/%Y')
    title = models.CharField(max_length=255)
    desc = models.TextField()
    button_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Contact(models.Model):
    fname = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.fname
