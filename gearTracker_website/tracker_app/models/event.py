from django.db import models


class Event(models.Model):
	"""
	Purpose: The Event model will allow users to create an Event Type(Category). ie: wedding, proposal, engagement

	Properties: name
	
	Methods: __str__ Returns an event name
	"""

	name = models.CharField(max_length=70)
	
	def __str__(self):
		return "{}".format(self.name)