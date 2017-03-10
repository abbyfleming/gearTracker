from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from tracker_app.models.customer import Customer
from tracker_app.models.lens_brand import LensBrand
from tracker_app.models.lens import Lens


# python manage.py test tracker_app

class TestCameraBrand(TestCase):
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

		
		self.nikkor = LensBrand(
			lens_brand_name = "Nikkor"
			)

		self.zoom = Lens(
			customer = self.suzy,
			lens_brand = self.nikkor,
			min_focal_length = 70,
			max_focal_length = 200,
			aperature = 2.8,
			purchase_date = "2011-07-01"
			)


	def test_zoom_is_instance_of_lens(self):
		self.assertIsInstance(self.zoom, Lens)
	
	def test_lens_has_customer(self):
		self.assertEqual("Suzy", self.zoom.customer.user.first_name)	

	def test_lens_has_brand(self):
		self.assertEqual("Nikkor", self.zoom.lens_brand.lens_brand_name)

	def test_lens_has_min_focal_length(self):
		self.assertEqual(70, self.zoom.min_focal_length)

	def test_lens_has_max_focal_length(self):
		self.assertEqual(200, self.zoom.max_focal_length)

	def test_lens_has_aperature(self):
		self.assertEqual(2.8, self.zoom.aperature)

	def test_lens_has_purchase_date(self):
		self.assertEqual("2011-07-01", self.zoom.purchase_date)
	

	