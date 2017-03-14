from django.db import models
from .customer import Customer
from .lens_make import LensMake
from .camera_make import CameraMake



class LensModel(models.Model):
	"""
	Author: @abbyfleming
	
	Purpose: The lens model will hold information to allow a customer to input their lens information.

	Properties: 
	
	Methods: __str__ Returns a lens brand name
	"""

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	mount = models.ForeignKey(CameraMake, on_delete=models.CASCADE)
	lens_make = models.ForeignKey(LensMake, on_delete=models.CASCADE)
	min_focal_length = models.PositiveIntegerField()
	max_focal_length = models.PositiveIntegerField()
	aperature = models.DecimalField(decimal_places=1, max_digits=5)
	purchase_date = models.DateField(auto_now=False)

	
	def __str__(self):
		return "{} {} {} {} {}".format(
							self.mount.name,
							self.lens_make.name, 
							self.min_focal_length, 
							self.max_focal_length,
							self.aperature)