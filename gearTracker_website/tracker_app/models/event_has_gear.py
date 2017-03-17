from django.db import models

from .event import Event
from .camera_model import CameraModel
from .lens_model import LensModel

class PhotoshootHasGear(models.Model):


	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	camera = models.ManyToManyField(CameraModel,blank=True)
	lens = models.ManyToManyField(LensModel,blank=True)

	def __str__(self):
		return "{}".format(self.event.name)

