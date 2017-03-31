from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from tracker_app.models.camera_make import CameraMake
import datetime

# python manage.py test tracker_app

class TestCameraMake(TestCase):
	'''
	Purpose: TestCameraMake

	Tests: 
		test_nikon_is_instance_of_camera_brand
		test_camera_has_brand_has_name
	'''

	@classmethod
	def setUpTestData(self):
		
		self.nikon = CameraMake(
			name = "Nikon"
			)


	def test_nikon_is_instance_of_camera_brand(self):
		self.assertIsInstance(self.nikon, CameraMake)
	
	def test_camera_has_brand_has_name(self):
		self.assertEqual("Nikon", self.nikon.name)

	

	