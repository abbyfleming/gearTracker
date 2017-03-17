from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import LensMake
from tracker_app.models import LensModel
from tracker_app.models import CameraMake
from tracker_app.models import Customer


class PhotoShootView(TemplateView):
    """
    Purpose: LENS MODEL: Nikon Nikkor 70-200 2.8
    Methods: post, get
    """

    template_name = 'photoshoot.html'

    def get(self, request):

        # Fetch the camera brands
        self.all_lens_makes = LensMake.objects.all()
        self.all_camera_makes = CameraMake.objects.all()
        
        return render(
            request, 'photoshoot.html',
            {'lens_make': self.all_lens_makes,
            'camera_make':self.all_camera_makes}
            )


    def post(self, request):
        data = request.POST

        # Fetch the data from the Form
        make = data['lens_list']
        mount = data['camera_list']
        date = data['purchase_date']
        min_focal = data['min_focal']
        max_focal = data['max_focal']
        aperature = data['aperature']
        purchase = data['purchase_date']
    
        # Find the values of the FK
        customer = Customer.objects.get(user=request.user.pk) 
        camera = CameraMake.objects.get(pk=mount)    
        lens = LensMake.objects.get(pk=make)


        # Redirect to same page
        return HttpResponseRedirect("/add-lens")


    
    

  