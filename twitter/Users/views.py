from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
@login_required
def HomePage(request):
    return(HttpResponse("HomePage"))

def SignIn(request):
    return(HttpResponse("Sign-In"))

def SignUp(request):
    if(request.method=="POST"):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('HomePage')

        msg=messages.add_message(request,messages.INFO,'Invalid Credentials')
        form=UserCreationForm()
        return(render(request,'Sign-Up.html',{'form':form}))

    else:
        form=UserCreationForm()
        msg=messages.add_message(request,messages.INFO,'Fill the FORM')
        return(render(request,'Sign-Up.html',{'form':form}))