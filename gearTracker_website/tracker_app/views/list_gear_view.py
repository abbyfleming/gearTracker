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
        self.all_camera = CameraModel.objects.filter(customer=request.user.pk).filter(missing=True)
        self.all_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=True)

        #MISSING
        self.missing_camera = CameraModel.objects.filter(customer=request.user.pk).filter(missing=False)        
        self.missing_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=False)


        return render(
            request, 'list_gear.html',{
            'camera': self.all_camera,
            'lens': self.all_lens,
            'missing_camera': self.missing_camera,
            'missing_lens': self.missing_lens,
            })



    def post(self, request):
        camera = request.POST.getlist('camera')
        print("*****camera*****", camera)

        lens = request.POST.getlist('lens')
        print("*****lens*****", lens)

        # REFACTOR
        self.all_camera = CameraModel.objects.filter(customer=request.user.pk).filter(missing=True)
        self.all_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=True)

        #MISSING
        self.missing_camera = CameraModel.objects.filter(customer=request.user.pk).filter(missing=False)
        self.missing_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=False)

        # Update gear to packed
        for c in camera:
            pack_camera = CameraModel.objects.filter(pk=c).update(missing=True)
   
        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l).update(missing=True)

        return render(
            request, 'list_gear.html',{
            'camera': self.all_camera,
            'lens': self.all_lens,
            'missing_camera': self.missing_camera,
            'missing_lens': self.missing_lens,
            })






    
    

  