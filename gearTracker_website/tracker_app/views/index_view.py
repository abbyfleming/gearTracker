from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.utils.timezone import datetime

from tracker_app.models import Event
from tracker_app.models import LensModel
from tracker_app.models import Photoshoot

class Index(TemplateView):
	''' 
	Purpose:
			Index view (homepage). Allows users to see current photoshoots, and limited list of gear

	get: 
			Returns photoshoot and lens. Limits all to last 3    
	'''
	
	template_name = "index.html"	
	
	def get(self, request):
		today = datetime.now()
		all_lens = LensModel.objects.all().filter(customer=request.user.pk)[:3]
		customer_photoshoot = Photoshoot.objects.filter(customer=request.user.pk).filter(date__gte=today).order_by('date')[:3]

		return render(request, self.template_name, {
				'customer_photoshoot': customer_photoshoot,
				'lens': all_lens,
				})

