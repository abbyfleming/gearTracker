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


class ReturnGearView(TemplateView):
    """
    Purpose: Given a user wants to to return their gear, check to make sure that all gear has been packed.
    If the gear has been packed, proceed to "success", otherwise flag missing gear as "missing"
    Methods: post, get
    """

    template_name = 'create_return_gear.html'

    
    def get(self, request, id):        
        # Fetch the event
        self.current_user = request.user.pk 
        self.photoshoot = Photoshoot.objects.get(pk=id)
        self.gear_id= Photoshoot.objects.filter(pk=id).values('gear_id')
        self.event_id = PhotoshootHasGear.objects.filter(pk=self.gear_id).values('event_id')
        self.event = Event.objects.get(pk=self.event_id)

        # GEAR
        self.gear = PhotoshootHasGear.objects.get(pk=self.gear_id)
        self.camera = self.gear.camera.filter(customer=request.user.pk)
        self.lens = self.gear.lens.filter(customer=request.user.pk)

        return render(
            request, 'create_return_gear.html',{
            'client_details': self.photoshoot,
            'event': self.event,
            'camera': self.camera,
            'lens': self.lens,
            }
            )



    def post(self, request, id):
        # Get data from Form
        camera = request.POST.getlist('camera')        
        lens = request.POST.getlist('lens')

        # PHOTOSHOOT
        self.photoshoot = Photoshoot.objects.get(pk=id)
        self.gear_id= Photoshoot.objects.filter(pk=id).values('gear_id')
        self.event_id = PhotoshootHasGear.objects.filter(pk=self.gear_id).values('event_id')
        self.event = Event.objects.get(pk=self.event_id)


        #Update gear that's been clicked to safe
        for c in camera:
            pack_camera = CameraModel.objects.filter(pk=c).update(safely_packed=True)
   
        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l).update(safely_packed=True)


        # Check to see if all gear has been packed
        gear = PhotoshootHasGear.objects.get(pk=self.gear_id)
        missing_camera = gear.camera.filter(safely_packed=False)
        missing_lens = gear.lens.filter(safely_packed=False)
        message = []
        

        # If all gear packed, redirect
        if (missing_lens.count() == 0) and (missing_camera.count() == 0):            
            # If all gear packed, set shoot to inactive
            # active_photoshoot = Photoshoot.objects.filter(id=id).update(active=False)
            return HttpResponseRedirect(redirect_to='/success')

        # Else display error message flat gear as missing
        else:  
            
            message = "Marked As Missing" 

            for c in missing_camera:
                flag_missing_camera = CameraModel.objects.filter(pk=c.pk).update(missing=True)
   
            for l in missing_lens:
                flag_missing_lens = LensModel.objects.filter(pk=l.pk).update(missing=True)
                
            
            return render(
                request, 'create_return_gear.html',{
                'message': message,
                'client_details': self.photoshoot,
                'event': self.event,
                'camera': missing_camera,
                'lens': missing_lens,
                })
