from django.views.generic.base import TemplateView
from django.shortcuts import render

from tracker_app.models import Event
from tracker_app.models import LensModel
from tracker_app.models import PhotoshootHasGear

class SuccessView(TemplateView):
	''' 
	Purpose:
		Success message
	'''

	template_name = "success.html"	

