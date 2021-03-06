from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField()
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', null=True)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()



class Project(models.Model):
    title = models.TextField(max_length=30)
    image = CloudinaryField('image')
    link= models.URLField(max_length=200)
    description = models.TextField(max_length=300)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    date_craeted= models.DateField(auto_now_add=True) 



    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    def __str__(self):
        return self.title