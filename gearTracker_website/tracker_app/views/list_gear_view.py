from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import CameraModel
from tracker_app.models import LensModel
from tracker_app.models import Customer


class ListGearView(TemplateView):
    """
    Purpose: CAMERA MODEL: D750, D700... 
    Methods: post, get
    Author: @abbyfleming
    """

    template_name = 'list_gear.html'

    def get(self, request):

        #CAMERA / LENS // REFACTOR
        self.all_camera = CameraModel.objects.filter(customer=request.user.pk).filter(missing=False)
        self.all_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=False)

        #MISSING
        self.missing_camera = CameraModel.objects.filter(customer=request.user.pk).filter(missing=True)
        self.missing_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=True)

        return render(
            request, 'list_gear.html',{
            'camera': self.all_camera,
            'lens': self.all_lens,
            'missing_camera': self.missing_camera,
            'missing_lens': self.missing_lens,
            })



    def post(self, request):
        camera = request.POST.getlist('camera')
        lens = request.POST.getlist('lens')
    
        # CAMERA/LENS
        all_camera = CameraModel.objects.filter(customer=request.user.pk).filter(missing=False)
        all_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=False)

        #MISSING
        missing_camera = CameraModel.objects.filter(customer=request.user.pk).filter(missing=True)
        missing_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=True)
    
        #Update gear to found and safe
        for c in camera:
            pack_camera = CameraModel.objects.filter(pk=c).update(missing=False, safely_packed=True)
   
        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l).update(missing=False, safely_packed=True)

        return render(
            request, 'list_gear.html',{
            'camera': all_camera,
            'lens': all_lens,
            'missing_camera': missing_camera,
            'missing_lens': missing_lens,
            })






    
    

  