from typing import Text
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import Post, User

class New_post_form(forms.Form):
    post_text = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Text'}), required=True)


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

#Hacer las funciones que envien los datos a las vistas. 

#Hacer las funciones que procesen las fetch request 

def new_post_view(request):
    
    if request.method == "GET":
        
        #Cambiar el index
        return render(request, "network/new_post.html", {
            "form": New_post_form()
        })
    
    elif request.method == "POST":
        
        if request.user.is_authenticated:
                            
            form = New_post_form(request.POST)
            
            if form.is_valid():
                
                post_text = form.cleaned_data["post_text"]
                
            
                new_post = Post.objects.create(
                    user = request.user,
                    text = post_text
                    
                )
                
                new_post.save()
                
                return HttpResponseRedirect(reverse("index"))
        else:
            pass
        