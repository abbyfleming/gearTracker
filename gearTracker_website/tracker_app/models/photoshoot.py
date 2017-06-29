from django.db import models
from .customer import Customer
from .event_has_gear import PhotoshootHasGear


class Photoshoot(models.Model):
	'''
	Purpose: 
		The Photoshoot model defines the structure of a photoshoot
	
	Properties: 
		customer - ForeignKey to Customer
		gear - ForeignKey to PhotoshootHasGear
		client_name - CharField
		location - CharField
		date - DateField
		active - BooleanField
		
	Methods:
		__str__ Returns client_name, gear.id (ie: Kasey 1)
	'''

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	gear = models.ForeignKey(PhotoshootHasGear, on_delete=models.CASCADE)
	client_name = models.CharField(max_length=70)
	location = models.CharField(max_length=140)
	date =  models.DateField(auto_now=False, auto_now_add=False, null=True , blank=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return "{} {}".format(self.client_name, self.gear.id)
