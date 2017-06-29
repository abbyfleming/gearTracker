from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect


from tracker_app.models import LensModel
from tracker_app.models import Customer
from tracker_app.models import PhotoshootHasGear
from tracker_app.models import Event
from tracker_app.models import Photoshoot


class ReturnGearView(TemplateView):
    ''' 
    Purpose:
        Allow a user to return their gear for an event. Flag gear as "missing" if an item isn't returned

    get:
        Returns client details, event, lens
    
    post:
        Selected items will be updated to safely_packed
        If missing, update to missing
        Return message if missing
    '''

    template_name = 'create_return_gear.html'

    def get(self, request, id):        
        
        # Fetch the event
        current_user = request.user.pk 
        photoshoot = Photoshoot.objects.get(pk=id)
        gear_id= Photoshoot.objects.filter(pk=id).values('gear_id')
        event_id = PhotoshootHasGear.objects.filter(pk=gear_id).values('event_id')
        event = Event.objects.get(pk=event_id)

        # GEAR
        gear = PhotoshootHasGear.objects.get(pk=gear_id)
        lens = gear.lens.filter(customer=request.user.pk)

        return render(request, self.template_name, {
            'client_details': photoshoot,
            'event': event,
            'lens': lens,
            })



    def post(self, request, id):
        # Get data from Form
        lens = request.POST.getlist('lens')

        # PHOTOSHOOT
        photoshoot = Photoshoot.objects.get(pk=id)
        gear_id= Photoshoot.objects.filter(pk=id).values('gear_id')
        event_id = PhotoshootHasGear.objects.filter(pk=gear_id).values('event_id')
        event = Event.objects.get(pk=event_id)

        #Update gear that's been clicked to safe
        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l).update(safely_packed=True)

        # Check to see if all gear has been packed
        gear = PhotoshootHasGear.objects.get(pk=gear_id)
        missing_lens = gear.lens.filter(safely_packed=False)
        message = []
        
        # If all gear packed, redirect
        if (missing_lens.count() == 0):            
            # If all gear packed, set shoot to inactive
            # active_photoshoot = Photoshoot.objects.filter(id=id).update(active=False)
            return HttpResponseRedirect(redirect_to='/success')

        # Else display error message flat gear as missing
        else:  
            
            message = "Marked As Missing" 

            for l in missing_lens:
                flag_missing_lens = LensModel.objects.filter(pk=l.pk).update(missing=True)                
            
            return render(request, self.template_name,{
                'message': message,
                'client_details': photoshoot,
                'event': event,
                'lens': missing_lens,
                })
