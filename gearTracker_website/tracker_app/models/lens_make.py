from django.db import models


class LensMake(models.Model):
	'''
	Purpose: 
		The LensMake model defines the structure of an lens make. (ie: Sigma). 

	Properties: 
		name - CharField
		
	Methods:
		__str__ Returns name (ie: Sigma)
	'''

	name = models.CharField(max_length=70)
	
	def __str__(self):
		return "{}".format(self.name)