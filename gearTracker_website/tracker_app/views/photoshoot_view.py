from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.utils.timezone import datetime

from tracker_app.models import LensModel
from tracker_app.models import CameraModel
from tracker_app.models import Customer
from tracker_app.models import PhotoshootHasGear
from tracker_app.models import Event
from tracker_app.models import Photoshoot


class PhotoShootView(TemplateView):
    """
    Purpose: Bring gear to a shoot!
    Methods: post, get
    """

    template_name = 'create_photoshoot.html'

    def get(self, request):

        # Fetch the event // REFACTOR
        today = datetime.now()

        #current user
        self.current_customer = request.user.pk
        # Photoshoot should only show types of photoshoots that the user has created

        # get current camera
        self.camera = CameraModel.objects.filter(customer=self.current_customer)
        self.event = PhotoshootHasGear.objects.filter(camera=self.camera)        
        self.photoshoot = Photoshoot.objects.filter(customer=request.user.pk).filter(date__gte=today).order_by('date')

        return render(
            request, 'create_photoshoot.html',{
            'event': self.event,
            'photoshoot': self.photoshoot,
            })

    

    def post(self, request):
        data = request.POST
        current_user = Customer.objects.get(user=request.user.pk)

        # Fetch the data from the Form
        client_name = data['client_name']
        location = data['location']
        date =  data['date']
        gear = data['event']
        print("*****gear*****", gear)

        # gear = models.ForeignKey(PhotoshootHasGear, on_delete=models.CASCADE)
        current_gear = PhotoshootHasGear.objects.get(pk=gear)
        print("*****current_gear*****", current_gear)

        create_photoshoot = Photoshoot.objects.create(
            customer = current_user,
            gear = current_gear,
            client_name = client_name,
            location = location,
            date = date,
            )

        # Redirect to same page
        return HttpResponseRedirect("/")


    
    

  