from django.db import models
from .customer import Customer
from .camera_make import CameraMake


class CameraModel(models.Model):
	'''	
	Purpose: 
		The CameraModel model defines the structure of a camera model. 
	
	Properties: 
		customer - ForeignKey to Customer
		camera_make - ForeignKey to CameraMake
		name - CharField
		safely_packed - Boolean
		missing - Boolean
	
	Methods: 
		__str__ returns camera_make.name, name (ie: Nikon D700)
	'''

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	camera_make = models.ForeignKey(CameraMake, on_delete=models.CASCADE)
	name = models.CharField(max_length=35)
	safely_packed = models.BooleanField(default=True)
	missing = models.BooleanField(default=False)

	def __str__(self):
		return "{} {}".format(self.camera_make.name, self.name)
