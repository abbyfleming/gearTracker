from django.views.generic.base import TemplateView
from django.shortcuts import render

from tracker_app.models import Event
from tracker_app.models import CameraModel
from tracker_app.models import LensModel
from tracker_app.models import PhotoshootHasGear

class Index(TemplateView):
  '''
  Purpose:
  Methods:
  Author:
  '''
  template_name = "index.html"	

  def get(self, request):
    
    self.customer_event = PhotoshootHasGear.objects.all()
    self.all_camera = CameraModel.objects.all().filter(customer=request.user.pk)
    self.all_lens = LensModel.objects.all().filter(customer=request.user.pk)

    # Note to self: Sort by date for events:
    # queryset = StoreEvent.objects.filter(stores__user=request.user).order_by('-date')
    # http://stackoverflow.com/questions/761352/django-queryset-order

    return render(
        request, 'index.html',{
        'event': self.customer_event,
        'camera': self.all_camera,
        'lens': self.all_lens,
        }
        )