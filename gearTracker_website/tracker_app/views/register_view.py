from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect

from tracker_app.models import Customer
from tracker_app.views import login_view



class Register(TemplateView):
    template_name = 'register.html'



def register_customer(request):
    """
    Purpose: Register a customer and immediently login
    Author: Abby
    """
    # create_user is what holds the username/password. (Django magic)
    # then, we pass that into the 1:1 field on our model, Customer
    # send all of the information to login_customer on login_view.py

    data = request.POST

    new_user = User.objects.create_user(
        username = data['username'], 
        email = data['email'],
        password = data['password'],
        first_name = data['first_name'],
        last_name = data['last_name'],
        )

    Customer.objects.create(
        user = new_user,
        )

    return login_view.login_customer(request)