from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from comptes.models import User,Discussion
from . import forms
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

#.................................................................
#class logout

def logout_user(request):
    
    logout(request)
    return redirect('login')
#.........................................................................    
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('index')
        message = 'Identifiants invalides.'
    return render(request, 'login.html', context={'form': form, 'message': message})
#.........................................................................    

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST or None, request.FILES)
        if form.is_valid():
            user = form.save()
            # auto-login user
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'inscription.html', context={'form': form})    
#..............................................

def discussion(request,user_id):
    user=User.objects.get(id=user_id)
    if request.method=="POST":
        message=request.POST["message"]
        Discussion.objects.create(
            message=message,
            sender=request.user,
            receiver=user
        )
    msg = Discussion.objects.filter(Q(sender = request.user, receiver = user) | Q(sender = user, receiver = request.user)).order_by("id")
    context={
        'userp':user,
        'messages' : msg
    }

    print(context)
    return render(request,'messagerie.html',context)
#........................................................

def mes(request,user_id):
    user=User.objects.get(id=user_id)
    discussion = Discussion.objects.filter(Q(sender = request.user) | Q(receiver = request.user)).distinct("sender")
    discussions = []
    senderReceiver = []
    for d in discussion :
        if d.sender not in senderReceiver:
            discussions.append(d)
            senderReceiver.append(d.sender)
            senderReceiver.append(d.receiver)
    return render(request,'mes.html', {"discussion" : discussions})