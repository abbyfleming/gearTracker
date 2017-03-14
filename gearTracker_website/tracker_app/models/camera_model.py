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
				purchase_date - datefield, optional
					
	Methods: __str__ Returns a customer's first and last name  
	"""

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	camera_model = models.ForeignKey(CameraMake, on_delete=models.CASCADE)
	name = models.CharField(max_length=35)
	purchase_date =  models.DateField(auto_now=False, auto_now_add=False, null=True , blank=True)

	def __str__(self):
		return "{} {}".format(self.camera_make.name, self.name)
