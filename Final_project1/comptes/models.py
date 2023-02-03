from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

# # Create your models here.
class User(AbstractUser):
    pass
    role=(
        ('Client','Client'),
        ('Prestataire','Prestataire')
    )
    role= models.CharField(max_length=20, choices=role)
    profile_photo = models.ImageField(verbose_name='photo de profil',blank=True)
    tel=models.CharField(max_length=17)
    description=models.TextField(max_length=100)

    Profil=(
        ('developpeur','developpeur'),
        ('graphiste','graphiste')
    )
    Profil=models.CharField(max_length=20,choices=Profil)

class Discussion(models.Model):
    message=models.TextField()
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='discussion_send')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='discussion_receive')

    