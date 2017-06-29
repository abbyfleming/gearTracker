from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.utils.timezone import datetime

from tracker_app.models import LensModel
from tracker_app.models import Customer
from tracker_app.models import PhotoshootHasGear
from tracker_app.models import Event
from tracker_app.models import Photoshoot


class PhotoShootView(TemplateView):
    ''' 
    Purpose:
        Allow a user to create a photoshoot with details

    get:
        Returns events (greater than today), photoshoot
    
    post:
        Create photoshoot details, event, and date
    '''

    template_name = 'create_photoshoot.html'

    def get(self, request):

        # Fetch the event // REFACTOR
        today = datetime.now()

        #current user
        current_customer = request.user.pk

        # get current 
        lens = LensModel.objects.filter(customer=request.user.pk)
        event = PhotoshootHasGear.objects.filter(lens=lens)

        photoshoot = Photoshoot.objects.filter(customer=request.user.pk).filter(date__gte=today).order_by('date')

        return render(request, self.template_name, {
            'event': event,
            'photoshoot': photoshoot,
            })

    

    def post(self, request):
        data = request.POST
        current_user = Customer.objects.get(user=request.user.pk)

        # Fetch the data from the Form
        client_name = data['client_name']
        location = data['location']
        date =  data['date']
        gear = data['event']

        # FK
        current_gear = PhotoshootHasGear.objects.get(pk=gear)

        create_photoshoot = Photoshoot.objects.create(
            customer = current_user,
            gear = current_gear,
            client_name = client_name,
            location = location,
            date = date,
            )

        # Redirect to same page
        return HttpResponseRedirect("/photoshoot")
