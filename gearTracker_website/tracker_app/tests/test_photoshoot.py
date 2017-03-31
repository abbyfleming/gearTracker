from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from tracker_app.models.customer import Customer
from tracker_app.models.lens_make import LensMake
from tracker_app.models.lens_model import LensModel
from tracker_app.models.camera_make import CameraMake
from tracker_app.models.camera_model import CameraModel
from tracker_app.models.event import Event
from tracker_app.models.event_has_gear import PhotoshootHasGear
from tracker_app.models.photoshoot import Photoshoot


# python manage.py test tracker_app

class TestPhotoshoot(TestCase):
	'''
	Purpose: TestPhotoshoot
	Tests: 

	'''

	@classmethod
	def setUpTestData(self):

		self.user = User(
			first_name = "Suzy",
			last_name = "Bishop",
			email = "s@s.com",
			username = "suzybishop",
			password="password1234"
			)
		self.user.save()


		self.suzy = Customer(
			user = self.user
			)
		self.suzy.save()

		
		self.nikkor = LensMake(
			name = "Nikkor"
			)
		self.nikkor.save()

		self.nikon = CameraMake(
			name = "Nikon"
			)
		self.nikon.save()

		self.zoom = LensModel(
			customer = self.suzy,
			mount = self.nikon,
			lens_make = self.nikkor,
			min_focal_length = 70,
			max_focal_length = 200,
			aperature = 2.8,
			)
		self.zoom.save()


		self.d700 = CameraModel(
			customer = self.suzy,
			camera_make = self.nikon,
			name = "D700",
			)
		self.d700.save()

		self.wedding = Event(
			name = "Wedding"
			)
		self.wedding.save()

		self.wedding_has_gear = PhotoshootHasGear.objects.create(
			event = self.wedding, 
			)
		self.wedding_has_gear.camera.add(self.d700)
		self.wedding_has_gear.lens.add(self.zoom)

		self.photoshoot = Photoshoot(
			customer = self.suzy,
			gear = self.wedding_has_gear,
			client_name = "Suzy Bishop",
			location = "Morning Camp, Rhode Island",
			date = "2017-05-01",
			active = "True"
			)
		self.photoshoot.save()



	

	