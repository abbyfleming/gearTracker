from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect


class Login(TemplateView):
    ''' 
    Purpose:
        Allow a user to login

    login_customer
    logout_view 

    '''
    
    template_name = 'login.html'


def login_customer(request):
    """
    Purpose: Login a customer using their username and password
    Author: Abby
    """
    data = request.POST

    username = data['username']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request=request, user=user)
    else:
        # Not successful, redirect to index page
        return HttpResponseRedirect(redirect_to='/')
    # Successful, redirect to view the products
    return HttpResponseRedirect(redirect_to='/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/')