from django.db import models
from .customer import Customer
from .camera_make import CameraMake


class CameraModel(models.Model):
	"""
	Author: @abbyfleming
	
	Purpose: The Camera model will hold information to allow a customer to input their camera information.

	Properties: customer - FK to customer
				camera_model - FK to camera model
				camera_make - string		
	Methods: 
	"""

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	camera_make = models.ForeignKey(CameraMake, on_delete=models.CASCADE)
	name = models.CharField(max_length=35)
	safely_packed = models.BooleanField(default=True)
	missing = models.BooleanField(default=False)

	def __str__(self):
		return "{} {}".format(self.camera_make.name, self.name)
