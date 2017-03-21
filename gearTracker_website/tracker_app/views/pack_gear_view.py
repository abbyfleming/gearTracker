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
        print("*****id*****", id) #2
        self.current_user = request.user.pk 

        #Get only photoshoot that's been clicked
        self.photoshoot = Photoshoot.objects.get(id=id)

        # Get the event type
        self.event_id = PhotoshootHasGear.objects.filter(id=id).values('event_id')
        print("*****self.event_id*****", self.event_id)
        
        self.event = Event.objects.get(id=self.event_id)
        print("*****self.event*****", self.event)

        # Get the Gear
        self.gear = PhotoshootHasGear.objects.get(event_id=self.event_id)
        self.camera = self.gear.camera.all().filter(customer_id=self.current_user)
        print("*****self.camera*****", self.camera)
        self.lens = self.gear.lens.all()

        return render(
            request, 'create_pack_gear.html',{
            'client_details': self.photoshoot,
            'event': self.event,
            'camera': self.camera,
            'lens': self.lens,
            }
            )



    def post(self, request, id):
        camera = request.POST.getlist('camera')
        lens = request.POST.getlist('lens')

        #update gear to packed
        for c in camera:
            pack_camera = CameraModel.objects.filter(pk=c).update(safely_packed=True)
            print("*****pack_camera*****", pack_camera)
            print("*****c*****", c)        

        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l).update(safely_packed=True)
            print("*****pack_lens*****", pack_lens)
            print("*****l*****", l)


        self.event_id = PhotoshootHasGear.objects.filter(id=id).values('event_id')
        print("*****self.event_id*****", self.event_id)
        # self.event = Event.objects.get(id=self.event_id)

        self.gear = PhotoshootHasGear.objects.get(event_id=self.event_id)
        self.camera = self.gear.camera.all().filter(safely_packed=False)
        self.lens = self.gear.lens.all().filter(safely_packed=False)
        print("*****self.gear*****", self.gear)
        print("*****self.camera*****", self.camera)
        print("*****self.lens*****", self.lens)

        # if self.camera.count() == 0:
        #     print("***you've packed all the cameras***")
        # else: 
        #     print("*****you missed a lens*****")     

        if (self.lens.count() == 0) and (self.camera.count() == 0):
            print("***you've packed everything")
        else:
            print("*****you missed*****")

        return HttpResponseRedirect(redirect_to='/')

