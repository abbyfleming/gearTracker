from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import CameraMake


class CameraMakeView(TemplateView):
    """
    Purpose: CAMERA MAKE: Nikon, Cannon...
    Methods: post, get
    Author: @abbyfleming
    """

    template_name = 'create_camera_make.html'

    def get(self, request):

        self.all_camera_make = CameraMake.objects.all()

        return render(
            request, 'create_camera_make.html', {
            'camera_make': self.all_camera_make,
            })



    def post(self, request):
        data = request.POST

        name = data['camera_make']

        create_camera_brand = CameraMake.objects.create(
            name=name,
            )

        # Redirect to same page
        return HttpResponseRedirect("/add-camera-make")


    
    

  