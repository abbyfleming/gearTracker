from django.test import TestCase
from django.contrib.auth.models import User

import sys
sys.path.append('../')

from tracker_app.models.lens_make import LensMake



class TestLensMake(TestCase):
	"""
	Purpose: Test Brand
	Author: Abby
	Tests:
		test_nikkor_is_instance_of_lens_brand
		test_lens_brand_has_name
	"""

	@classmethod
	def setUpTestData(self):

		self.nikkor = LensMake(
			name = "Nikkor"
			)

	def test_nikkor_is_instance_of_lens_brand(self):
		self.assertIsInstance(self.nikkor, LensMake)

	def test_lens_brand_has_name(self):
		self.assertEqual("Nikkor", self.nikkor.name)