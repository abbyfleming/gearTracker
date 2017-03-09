from django.db import models
from .customer import Customer
from .camera_brand import CameraBrand


class Camera(models.Model):
	"""
	Author: @abbyfleming
	
	Purpose: The Camera model will hold information to allow a customer to input their camera information.

	Properties: customer - FK to customer
				camera_brand - FK to camera brand
				camera_model - string
				purchase_date - datefield
					
	Methods: __str__ Returns a customer's first and last name  
	"""

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	camera_brand = models.ForeignKey(CameraBrand, on_delete=models.CASCADE)
	camera_model = models.CharField(max_length=35)
	purchase_date =  models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return "{} {}".format(self.camera_brand.name, self.camera_model)
