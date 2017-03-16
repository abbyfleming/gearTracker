from django.db import models
from .customer import Customer
from .camera_make import CameraMake
from .event_has_gear import PhotoshootHasGear


class Photoshoot(models.Model):
	"""
	Purpose: The Camera model will hold information to allow a customer to input their camera information.

	Properties: 
					
	Methods: __str__ Returns a customer's first and last name  
	"""

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	gear = models.ForeignKey(PhotoshootHasGear, on_delete=models.CASCADE)
	client_name = models.CharField(max_length=70)
	location = models.CharField(max_length=140)
	date =  models.DateField(auto_now=False, auto_now_add=False, null=True , blank=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return "{} {}".format(self.camera_make.name, self.name)
