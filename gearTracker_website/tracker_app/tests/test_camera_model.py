from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from tracker_app.models.customer import Customer
from tracker_app.models.camera_make import CameraMake
from tracker_app.models.camera_model import CameraModel

import datetime

# python manage.py test tracker_app

class TestCameraModel(TestCase):
	"""
	Purpose: Test Customer
	Author: Abby
	Tests: 
		test_d700_is_instance_of_camera
		test_camera_has_customer
		test_camera_has_brand
		test_camera_has_model
		test_camera_has_purchase_date
	"""

	@classmethod
	def setUpTestData(self):

		self.user = User(
			first_name = "Suzy",
			last_name = "Bishop",
			email = "s@s.com",
			username = "suzybishop",
			password="password1234"
			)


		self.suzy = Customer(
			user = self.user
			)

		
		self.nikon = CameraMake(
			name = "Nikon"
			)

		self.d700 = CameraModel(
			customer = self.suzy,
			camera_make = self.nikon,
			name = "D700",
			purchase_date =  "2010-06-01",
			)


	def test_d700_is_instance_of_camera(self):
		self.assertIsInstance(self.d700, CameraModel)
	
	def test_camera_has_customer(self):
		self.assertEqual("Suzy", self.d700.customer.user.first_name)

	def test_camera_has_brand(self):
		self.assertEqual("Nikon", self.d700.camera_make.name)

	def test_camera_has_model(self):
		self.assertEqual("D700", self.d700.name)

	def test_camera_has_purchase_date(self):
		self.assertEqual("2010-06-01", self.d700.purchase_date)
	

	