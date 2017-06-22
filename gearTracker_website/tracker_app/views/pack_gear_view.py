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
        photoshoot = Photoshoot.objects.get(pk=id)
        gear_id= Photoshoot.objects.filter(pk=id).values('gear_id')
        event_id = PhotoshootHasGear.objects.filter(pk=gear_id).values('event_id')
        event = Event.objects.get(pk=event_id)

        # GEAR
        gear = PhotoshootHasGear.objects.get(pk=gear_id)
        camera = gear.camera.filter(customer=request.user.pk)
        lens = gear.lens.filter(customer=request.user.pk)

        return render(request, self.template_name, {
            'client_details': photoshoot,
            'event': event,
            'camera': camera,
            'lens': lens,
            })


    def post(self, request, id):

        # Get data from Form
        camera = request.POST.getlist('camera')
        lens = request.POST.getlist('lens')
        current_user = request.user.pk 
        
        # PHOTOSHOOT
        photoshoot = Photoshoot.objects.get(pk=id)
        gear_id= Photoshoot.objects.filter(pk=id).values('gear_id')
        event_id = PhotoshootHasGear.objects.filter(pk=gear_id).values('event_id')
        event = Event.objects.get(pk=event_id)

        # GEAR
        gear = PhotoshootHasGear.objects.get(pk=gear_id)
        camera = gear.camera.filter(safely_packed=True)
        lens = gear.lens.filter(safely_packed=True)
 
        # Update gear to packed
        for c in camera:
            pack_camera = CameraModel.objects.filter(pk=c.id).update(safely_packed=False)

        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l.id).update(safely_packed=False)


        message = []
        
        # LENS
        if (lens.count() == 0) and (camera.count() == 0):
            # If all gear packed, set shoot to active
            active_photoshoot = Photoshoot.objects.filter(id=id).update(active=True)
            return HttpResponseRedirect(redirect_to='/success')

        else:  
            # Display error message
            message = "Oops! Keep Packing"  

            return render(request, self.template_name,{
                'message': message,
                'event': event,
                'client_details': photoshoot,
                'camera': camera,
                'lens': lens,
                }
                )
