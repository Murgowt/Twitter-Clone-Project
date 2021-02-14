from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    followers=models.ManyToManyField(User,related_name='followers')
    following=models.ManyToManyField(User,related_name='following')

class Requests(models.Model):
    sender=models.ManyToManyField(User,related_name='sender')
    receiver=models.ManyToManyField(User,related_name='receiver')
    is_active=models.BooleanField(default=True)
    