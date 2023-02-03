from django.shortcuts import render
from comptes.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
"""from .forms import personneform"""
from .import forms
# Create your views here.

# def personne_list(request):
#     personne=User.objects.all()
#     context={
#         'personne':personne
#     }
    
#     print(context)
#     return render(request, 'homepage.html',context)

def graphiste(request):
    return render(request, 'graphiste.html')

def developpement(request):
    return render(request, 'developpement.html')

"""def Details(request):
    return render(request, 'Details.html')"""


def home(request):
    personne=User.objects.all()
    context={
        'personne':personne
    }
    print(personne)
    return render(request, 'homepage.html',context)

def base(request):
    personne=User.objects.all(id=id)
    context={
        'personne':personne
    }
    print(personne)
    return render(request, 'base.html',context)


def annonces(request):
    if not request.user.is_authenticated :
        return redirect("home")
    
    if not request.user.is_prestataire :
        return redirect("home")


    

def user_dashboard(request):

    if not request.user.is_authenticated :
        return redirect("home")

    personne=User.objects.all()
    context={
        'personnes':personne
    }
    user  = User.objects.get(id = 2)
    pr  = Profil.objects.get(id=1)
    pr.User.remove()
    
    if request.user.is_client :
        return render(request, 'client.html',context)
    
    if request.user.is_prestataire :
        return render(request, 'prestation.html',context)
    
    return render(request, 'notFound.html',context)
    



# connexion d'un utilisateur a un compte
def log_user (request) :
    # si le formulaire a ete rempli et envoye
    if request.method == "POST" :
        # recuperation des donnees saisies dans le formulaire
        email = request.POST["email"]
        password = request.POST["password"]
        # verifier si un utilisateur existe avec les informations saisies
        user = authenticate(request, username = email, password = password)
        print(user)
        if user:
            login(request, user)
            return redirect("home")
        return render(request, "base", {"msg": "utilisateur introuvable"})
    else : # sinon on lui envoi le formulaire de connexion
        return render(request, "base", {"msg" : " simple demande"})
        



def base_page(request):
    return render(request,"base.html")

def Details(request,user_id):
    personne=User.objects.filter(id=user_id)
    context={
        'personne':personne
    }
    return render(request,'Details.html',context)


def index(request):
    personnes=User.objects.all()
    context={
        'personnes':personnes
    }
    return render(request,"index.html", context)