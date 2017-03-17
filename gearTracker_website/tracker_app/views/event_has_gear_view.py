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
        data = request.POST
        print("*****data*****", data)
        
        # Event
        event = data['event']
        event_data = Event.objects.get(pk=event)
        print("*****event_data*****", event_data)
        
        # Create the Event
        event_has_gear = PhotoshootHasGear.objects.create(
            event = event_data,
        )
        print("*** EVENT HAS NAME", event_has_gear.event.name)

        # Lenses 
        lens = request.POST.getlist('lens')

        for l in lens:
            lens_data = LensModel.objects.get(pk=l)
            new_lens = event_has_gear.lens.add(lens_data)
            print("***get lens***", lens_data)        

        # Camera
        camera = request.POST.getlist('camera')
        
        for c in camera:
            camera_data = CameraModel.objects.get(pk=c)
            new_camera = event_has_gear.camera.add(camera_data)
            print("***get camera***", camera_data)


        # Redirect to same page
        return HttpResponseRedirect("/event-gear")


    
    

  