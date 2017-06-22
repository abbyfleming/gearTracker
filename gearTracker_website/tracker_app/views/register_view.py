from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect

from tracker_app.models import Customer
from tracker_app.views import login_view



class Register(TemplateView):
    ''' 
    Purpose:
        Allow a user to register using create_user

    register_customer - once registered, immediate login

    '''

    template_name = 'register.html'

def register_customer(request):
    data = request.POST

    new_user = User.objects.create_user(
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        username = data['username'], 
        password = data['password'],
        )

    Customer.objects.create(
        user = new_user,
        )

    return login_view.login_customer(request)


    