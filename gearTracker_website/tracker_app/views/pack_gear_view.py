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
    ''' 
    Purpose:
        Allow a user to pack their gear for an event. Notify user is gear has not been packed.

    get:
        Returns client details, event, camera, lens
    
    post:
        Update camera, lens to not safely packed (false)
        and add a message (if a gear item has not been packed)
    '''

    template_name = 'create_pack_gear.html'

    
    def get(self, request, id):

        # PHOTOSHOOT
        self.photoshoot = Photoshoot.objects.get(pk=id)
        self.gear_id= Photoshoot.objects.filter(pk=id).values('gear_id')
        self.event_id = PhotoshootHasGear.objects.filter(pk=self.gear_id).values('event_id')
        self.event = Event.objects.get(pk=self.event_id)

        # GEAR
        self.gear = PhotoshootHasGear.objects.get(pk=self.gear_id)
        self.camera = self.gear.camera.filter(customer=request.user.pk)
        self.lens = self.gear.lens.filter(customer=request.user.pk)

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
        
        # PHOTOSHOOT
        self.photoshoot = Photoshoot.objects.get(pk=id)
        self.gear_id= Photoshoot.objects.filter(pk=id).values('gear_id')
        self.event_id = PhotoshootHasGear.objects.filter(pk=self.gear_id).values('event_id')
        self.event = Event.objects.get(pk=self.event_id)

        # GEAR
        self.gear = PhotoshootHasGear.objects.get(pk=self.gear_id)
        self.camera = self.gear.camera.filter(safely_packed=True)
        self.lens = self.gear.lens.filter(safely_packed=True)
 
        # Update gear to packed
        for c in camera:
            pack_camera = CameraModel.objects.filter(pk=c).update(safely_packed=False)

   
        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l).update(safely_packed=False)

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
