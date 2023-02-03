from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#class personne

"""class Personne(AbstractUser):
    tel=models.CharField(max_length=17)
    image=models.ImageField(upload_to='Images',blank=True)
    role=(
        ('1','Client'),
        ('2','Prestataire')
    )
    role= models.CharField(max_length=1, choices=role)

    @property
    def is_client (self) :
        return self.role == '1'
    
    @property
    def is_prestataire (self) :
        return self.role == '2'

    @property
    def get_role (self) :
        if self.role == "1" :
            return "Cient"
        elif self.role == "2" :
            return 'Prestataire'"""




#class annonce

class Annonces(models.Model):
    titre=models.CharField(max_length=15)
    description=models.TextField()
    image=models.ImageField(upload_to='Images',blank=True)
    Personne=models.ForeignKey('comptes.User',on_delete=models.CASCADE)

#class profile

class Profil(models.Model):
    nomPr=models.CharField(max_length=30,blank=True)
    Personne=models.ManyToManyField('comptes.User', blank=True, related_name="profiles")
    Annonces=models.ManyToManyField(Annonces, blank=True)


#class candidatures

class Candidatures(models.Model):
    Personne=models.ForeignKey('comptes.User',on_delete=models.CASCADE)
    Annonces=models.ForeignKey(Annonces,on_delete=models.CASCADE)