from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect


from tracker_app.models import LensModel
from tracker_app.models import CameraModel
from tracker_app.models import Customer
from tracker_app.models import PhotoshootHasGear
from tracker_app.models import Event
from tracker_app.models import Photoshoot


class PackGearView(TemplateView):
    """
    Purpose: Bring gear to a shoot!
    Methods: post, get
    """

    template_name = 'create_pack_gear.html'

    
    def get(self, request, id):
        # Fetch the event

        # Get only photoshoot that's been clicked
        self.photoshoot = Photoshoot.objects.get(id=id)

        # Get the event type
        self.event_id = PhotoshootHasGear.objects.filter(id=id).values('event_id')
        self.event = Event.objects.get(id=self.event_id)

        # Get the Gear
        #self.gear_id = Photoshoot.objects.filter(gear_id=id).values('gear_id')
        self.gear = PhotoshootHasGear.objects.get(event_id=self.event_id)
        print("*****gear*****", self.gear)  
        
        self.camera = self.gear.camera.all()
        print("*****self.camera*****", self.camera)

        self.lens = self.gear.lens.all()
        print("*****self.lens*****", self.lens)


        return render(
            request, 'create_pack_gear.html',{
            'client_details': self.photoshoot,
            'event': self.event,
            'camera': self.camera,
            'lens': self.lens,
            }
            )


    # def post(self, request):
    #     data = request.POST
    #     print("*****data*****", data)

    #     #http://stackoverflow.com/questions/2417127/how-do-i-get-the-values-of-all-selected-checkboxes-in-a-django-request-post

    #     # Redirect to same page
    #     return HttpResponseRedirect("/pack-gear")


    
    

  