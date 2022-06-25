from email import message
from django.db import models

# Create your models here.
from email.policy import default
from django.db import models
import datetime
# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='team_images')
    facebook_link=models.URLField(max_length=100)
    twitter_link=models.URLField(max_length=100)
    instragram_link=models.URLField(max_length=100)
    linkedin_link=models.URLField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Register(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.IntegerField()
    confirm_password=models.IntegerField()

    def __str__(self):
        return self.username

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name
