from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import CameraBrand


class CameraBrandView(TemplateView):
    """
    Purpose: Post and get Camera Brands
    Methods: post, get
    Author: @abbyfleming
    """

    template_name = 'create_camera_brand.html'

    def get(self, request):

        self.all_camera_brands = CameraBrand.objects.all()

        return render(
            request, 'create_camera_brand.html',
            {'camera_brand': self.all_camera_brands,}
            )



    def post(self, request):
        data = request.POST

        brand = data['camera_brand']

        create_camera_brand = CameraBrand.objects.create(camera_brand_name=brand)

        # Redirect to same page
        return HttpResponseRedirect("/camera_brand")


    
    

  