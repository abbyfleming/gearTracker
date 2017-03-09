from django.db import models


class LensBrand(models.Model):
	"""
	Author: @abbyfleming
	
	Purpose: The Lens model will allow users to select from pre-defined camera choices. Example: Nikon

	Properties: lens_brand_name
	
	Methods: __str__ Returns a lens brand name
	"""

	lens_brand_name = models.CharField(max_length=70)
	
	def __str__(self):
		return "{}".format(self.lens_brand_name)