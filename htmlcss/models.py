from select import select
from django.db import models
# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=20)
    funame = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mobile = models.IntegerField()
    password = models.CharField(max_length=20)
    confirm_Password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    # def get_password(self):
    #     return self.password
    
    # def __str__(self):
    #     # return self.username
    #     return self.initial["password"]
    

class Profile(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE)
    token = models.CharField(max_length=150)
    verify = models.BooleanField(default=False)