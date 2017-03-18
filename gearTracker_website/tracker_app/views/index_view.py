from django.views.generic.base import TemplateView
from django.shortcuts import render

from tracker_app.models import Event
from tracker_app.models import CameraModel
from tracker_app.models import LensModel

class Index(TemplateView):
  '''
  Purpose:
  Methods:
  Author:
  '''
  template_name = "index.html"	

  def get(self, request):

    self.all_event = Event.objects.all()
    self.all_camera = CameraModel.objects.all().filter(customer=request.user.pk)
    self.all_lens = LensModel.objects.all().filter(customer=request.user.pk)

    print("*****self.all_lens*****", self.all_lens)

    return render(
        request, 'index.html',{
        'event': self.all_event,
        'camera': self.all_camera,
        'lens': self.all_lens,
        }
        )