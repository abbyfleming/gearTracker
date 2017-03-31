from django.db import models
from .customer import Customer
from .lens_make import LensMake
from .camera_make import CameraMake



class LensModel(models.Model):
	'''
	Purpose: 
		The LensModel model defines the structure of an lens model. Lenses have mounts (ie: Canon/Nikon), but can also have different makes (ie: Sigma/Tamron). 

	Properties: 
		customer - ForeignKey to Customer
		mount - ForeignKey to CameraMake
		lens_make - ForeignKey to LensMake
		min_focal_length - PositiveIntegerField
		max_focal_length - PositiveIntegerField
		aperature - DecimalField
		safely_packed - Boolean
		missing - Boolean
		
	Methods:
		__str__ Returns mount.name, lens_make.name, min_focal_length, max_focal_length, aperature
			ie: Nikon Nikkor 24 70 2.8
	'''

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	mount = models.ForeignKey(CameraMake, on_delete=models.CASCADE)
	lens_make = models.ForeignKey(LensMake, on_delete=models.CASCADE)
	min_focal_length = models.PositiveIntegerField()
	max_focal_length = models.PositiveIntegerField()
	aperature = models.DecimalField(decimal_places=1, max_digits=5)
	safely_packed = models.BooleanField(default=True)
	missing = models.BooleanField(default=False)

	
	def __str__(self):
		return "{} {} {} {} {}".format(
							self.mount.name,
							self.lens_make.name, 
							self.min_focal_length, 
							self.max_focal_length,
							self.aperature)

		