from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField( upload_to='profile/', blank ='true',default='default.png')
    bio = models.TextField()
    user =models.OneToOneField(User, on_delete = models.CASCADE)
    date_craeted= models.DateField(auto_now_add=True )

    def __str__(self):
        return f'{self.user.username} Profile'
