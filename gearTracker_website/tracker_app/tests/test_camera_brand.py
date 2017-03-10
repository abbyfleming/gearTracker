from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from tracker_app.models.camera_brand import CameraBrand
import datetime

# python manage.py test tracker_app

class TestCameraBrand(TestCase):
	"""
	Purpose: Test Customer
	Author: Abby
	Tests: 
		test_customer_is_instance
		test_customer_has_name
	"""

	@classmethod
	def setUpTestData(self):
		
		self.nikon = CameraBrand(
			camera_brand_name = "Nikon"
			)


	def test_nikon_is_instance_of_camera_brand(self):
		self.assertIsInstance(self.nikon, CameraBrand)
	
	def test_camera_has_brand_has_name(self):
		self.assertEqual("Nikon", self.nikon.camera_brand_name)

	

	