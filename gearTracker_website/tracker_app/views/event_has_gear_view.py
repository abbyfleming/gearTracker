from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import Customer
from tracker_app.models import Event
from tracker_app.models import LensModel
from tracker_app.models import CameraModel
from tracker_app.models import PhotoshootHasGear




class EventHasGearView(TemplateView):
    """
    Purpose: EVENT: Create an event ie: Wedding, Proposal
    Methods: post, get
    Author: @abbyfleming
    """

    template_name = 'create_event_gear.html'

    def get(self, request):

        self.all_events = Event.objects.all()
        self.all_lens = LensModel.objects.all()
        self.all_camera = CameraModel.objects.all()
        
        return render(
            request, 'create_event_gear.html', {
            'event': self.all_events,
            'lens': self.all_lens,
            'camera': self.all_camera,
            })


    def post(self, request):
        # data = request.POST
        # print("*****data*****", data)
        
        lens = request.POST.getlist('lens')
        print("*****lens*****", lens)
        
        camera = request.POST.getlist('camera')
        print("*****camera*****", camera)
        
        # Fetch the data from the form
        # event = data['event']
        
        for l in lens:
            print("***lens index****", l)

        for c in camera:
            print("***camera index***", c)

        # print("Type of lens", type(lens))

        # print("***first item in lens", data['lens'][0])

        #loop over lens and camera to pull the objects out.
        

        # Find the FK information
        # customer = Customer.objects.get(user=request.user.pk)
        # event = Event.objects.get(pk=e)
        # lens = LensModel.objects.get(pk=l)
        # camera = CameraModel.objects.get(pk=c)
          
        # create_event_has_gear = PhotoshootHasGear.objects.create(
        #     event = event,
        #     camera = camera,
        #     lens = lens,
        #     )

        # Redirect to same page
        return HttpResponseRedirect("/event-gear")


    
    

  