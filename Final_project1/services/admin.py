from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Annonces,Profil,Candidatures

# Register your models here.

admin.site.register([Annonces,Profil,Candidatures])
admin.site.unregister(Group)