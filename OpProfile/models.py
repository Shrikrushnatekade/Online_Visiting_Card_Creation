from django.db import models

# Create your models here.
class Businesscard:
    id : int
    name : str
    number : int
    emailu : str
    weurl : str
    street : str
    city : str
    state : str
    country : str
    business : str
    work : str
    Address : str
    twitter : str
    website : str

class SelfCard(models.Model):
    username = models.CharField(max_length=100)
    email1 = models.EmailField(max_length=100)
    place = models.CharField(max_length=100)
    shopname = models.CharField(max_length=100)
    number = models.IntegerField()
    fb = models.CharField(max_length=100)
    userimg = models.ImageField(upload_to="Userimage")
    date = models.DateTimeField(auto_now_add=True)