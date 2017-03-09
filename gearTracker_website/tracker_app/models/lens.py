from django.db import models
from .customer import Customer
from .lens_brand import LensBrand


class Lens(models.Model):
	"""
	Author: @abbyfleming
	
	Purpose: The Camera model will hold information to allow a customer to input their lens information.

	Properties: lens_brand_name
	
	Methods: __str__ Returns a lens brand name
	"""

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	lens_brand = models.ForeignKey(LensBrand, on_delete=models.CASCADE)
	min_focal_length = models.PositiveIntegerField()
	max_focal_length = models.PositiveIntegerField()
	aperature = models.DecimalField(decimal_places=1, max_digits=5)
	purchase_date = models.DateField(auto_now=False)

	
	def __str__(self):
		return "{} {} {} {}".format(
							self.lens_brand.lens_brand_name, 
							self.min_focal_length, 
							self.max_focal_length,
							self.aperature)