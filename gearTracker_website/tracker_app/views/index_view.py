from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.utils.timezone import datetime

from tracker_app.models import Event
from tracker_app.models import CameraModel
from tracker_app.models import LensModel
from tracker_app.models import Photoshoot

class Index(TemplateView):
  '''
  Purpose:
  Methods:
  Author:
  '''
  template_name = "index.html"	

  def get(self, request):
    today = datetime.now()

    self.all_camera = CameraModel.objects.all().filter(customer=request.user.pk)[:3]
    self.all_lens = LensModel.objects.all().filter(customer=request.user.pk)[:3]
    self.customer_photoshoot = Photoshoot.objects.filter(customer=request.user.pk).filter(date__gte=today).order_by('date')[:3]

    return render(
        request, 'index.html',{
        'customer_photoshoot': self.customer_photoshoot,
        'camera': self.all_camera,
        'lens': self.all_lens,
        }
        )