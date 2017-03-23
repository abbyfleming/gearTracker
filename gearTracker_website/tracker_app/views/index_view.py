from django.views.generic.base import TemplateView
from django.shortcuts import render

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

    self.all_camera = CameraModel.objects.all().filter(customer=request.user.pk)
    self.all_lens = LensModel.objects.all().filter(customer=request.user.pk)
    self.customer_photoshoot = Photoshoot.objects.filter(customer=request.user.pk).order_by('date')

    # Note to self: Sort by date for events:
    # queryset = StoreEvent.objects.filter(stores__user=request.user).order_by('-date')
    # http://stackoverflow.com/questions/761352/django-queryset-order

    return render(
        request, 'index.html',{
        'customer_photoshoot': self.customer_photoshoot,
        'camera': self.all_camera,
        'lens': self.all_lens,
        }
        )