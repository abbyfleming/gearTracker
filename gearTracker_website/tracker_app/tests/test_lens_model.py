from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from tracker_app.models.customer import Customer
from tracker_app.models.lens_make import LensMake
from tracker_app.models.lens_model import LensModel


# python manage.py test tracker_app

class TestLensModel(TestCase):
	'''
	Purpose: Test TestLensModel
	Tests: 
		test_zoom_is_instance_of_lens
		test_lens_has_customer
		test_lens_has_brand
		test_lens_has_min_focal_length
		test_lens_has_max_focal_length
		test_lens_has_aperature
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


		self.suzy = Customer(
			user = self.user
			)

		
		self.nikkor = LensMake(
			name = "Nikkor"
			)

		self.zoom = LensModel(
			customer = self.suzy,
			lens_make = self.nikkor,
			min_focal_length = 70,
			max_focal_length = 200,
			aperature = 2.8,
			)


	def test_zoom_is_instance_of_lens(self):
		self.assertIsInstance(self.zoom, LensModel)
	
	def test_lens_has_customer(self):
		self.assertEqual("Suzy", self.zoom.customer.user.first_name)	

	def test_lens_has_brand(self):
		self.assertEqual("Nikkor", self.zoom.lens_make.name)

	def test_lens_has_min_focal_length(self):
		self.assertEqual(70, self.zoom.min_focal_length)

	def test_lens_has_max_focal_length(self):
		self.assertEqual(200, self.zoom.max_focal_length)

	def test_lens_has_aperature(self):
		self.assertEqual(2.8, self.zoom.aperature)

	

	