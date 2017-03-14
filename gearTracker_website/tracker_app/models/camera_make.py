from django.db import models


class CameraMake(models.Model):
	"""
	Author: @abbyfleming
	
	Purpose: The Camera Brand model will allow users to select from pre-defined camera choices. Example: Nikon

	Properties: camera_brand_name
	
	Methods: __str__ Returns a camera brand name
	"""

	name = models.CharField(max_length=70)
	
	def __str__(self):
		return "{}".format(self.camera_make)
