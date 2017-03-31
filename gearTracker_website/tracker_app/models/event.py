from django.db import models


class Event(models.Model):
	'''
	Purpose: 
		The Event model defines the structure of an event. (ie: Wedding)

	Properties: 
		name - CharField
	
	Methods:
		__str__ Returns name (ie: Wedding)
	'''

	name = models.CharField(max_length=70)
	
	def __str__(self):
		return "{}".format(self.name)