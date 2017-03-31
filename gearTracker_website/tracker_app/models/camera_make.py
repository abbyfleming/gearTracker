from django.db import models


class CameraMake(models.Model):
	'''	
	Purpose: 
		The CameraModel model defines the structure of a camera make. 
	
	Properties: 
		name- CharField
	
	Methods: 
		__str__ returns a camera brand name (ie: Nikon)
	'''

	name = models.CharField(max_length=70)
	
	def __str__(self):
		return "{}".format(self.name)
