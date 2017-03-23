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
        self.current_user = request.user.pk 

        # #Get only photoshoot that's been clicked
        self.photoshoot = Photoshoot.objects.get(id=id)
        self.gear_id = Photoshoot.objects.filter(id=id).values('gear_id')
        self.event_id = PhotoshootHasGear.objects.filter(id=id).values('event_id')
        self.event = Event.objects.get(id=self.gear_id)

        # # Get the Gear
        self.gear = PhotoshootHasGear.objects.get(event_id=self.gear_id)
        self.camera = self.gear.camera.all().filter(customer_id=self.current_user)
        self.lens = self.gear.lens.all().filter(customer_id=self.current_user)

        return render(
            request, 'create_pack_gear.html',{
            'client_details': self.photoshoot,
            'event': self.event,
            'camera': self.camera,
            'lens': self.lens,
            })


    def post(self, request, id):
        # Get data from Form
        camera = request.POST.getlist('camera')
        lens = request.POST.getlist('lens')
        self.current_user = request.user.pk 

        print("*****camera*****", camera)
        print("*****lens*****", lens)
        
        # Get photoshoot data
        self.photoshoot = Photoshoot.objects.get(id=id)
        self.gear_id = Photoshoot.objects.filter(id=id).values('gear_id')
        self.event_id = PhotoshootHasGear.objects.filter(id=id).values('event_id')
        self.event = Event.objects.get(id=self.gear_id)
 
        # Update gear to packed
        for c in camera:
            pack_camera = CameraModel.objects.filter(pk=c).update(safely_packed=False)
   
        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l).update(safely_packed=False)
 

        # Check to see if all gear has been packed
        self.gear = PhotoshootHasGear.objects.get(event_id=self.gear_id)
        print("*****self.gear*****", self.gear)

        self.camera = self.gear.camera.all().filter(safely_packed=True)
        print("*****self.camera*****", self.camera)
        self.lens = self.gear.lens.all().filter(safely_packed=True)
        print("*****self.camera*****", self.camera)
        self.message = []
        
        # LENS
        if (self.lens.count() == 0) and (self.camera.count() == 0):
            # If all gear packed, set shoot to active
            active_photoshoot = Photoshoot.objects.filter(id=id).update(active=True)
            return HttpResponseRedirect(redirect_to='/success')

        else:  
            # Display error message and list of items that returned False
            self.message = "Oops! Keep Packing"  

            return render(
                request, 'create_pack_gear.html',{
                'message': self.message,
                'event': self.event,
                'client_details': self.photoshoot,
                'camera': self.camera,
                'lens': self.lens,
                }
                )
