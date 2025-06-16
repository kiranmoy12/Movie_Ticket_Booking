from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone=models.IntegerField(unique=True, null=True,blank=True)
    is_theater_manager =models.BooleanField(default=False,null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    otp = models.IntegerField(null=True,blank=True)
    otp_verify = models.BooleanField(null=True,blank=True)
    otp_expire = models.DateTimeField(null=True,blank=True)

