from django.db import models

from .event import Event
from .lens_model import LensModel

class PhotoshootHasGear(models.Model):
	'''
	Purpose: 
		The PhotoshootHasGear model defines the structure of an event's gear. (ie: A wedding has lenses associated.) This model allows a user to make a list of gear for specific events.

	Properties: 
		event - ForeignKey to Event
		lens - ManyToManyField to LensModel

	Methods:
		__str__ Returns event name (ie: Wedding)
	'''


	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	lens = models.ManyToManyField(LensModel,blank=True)

	def __str__(self):
		return "{}".format(self.event.name)

