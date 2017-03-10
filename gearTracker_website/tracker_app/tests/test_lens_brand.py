from django.test import TestCase
from django.contrib.auth.models import User

import sys
sys.path.append('../')

from tracker_app.models.lens_brand import LensBrand



class TestLensBrand(TestCase):
	"""
	Purpose: Test Brand
	Author: Abby
	Tests:
		test_nikkor_is_instance_of_lens_brand
		test_lens_brand_has_name
	"""

	@classmethod
	def setUpTestData(self):

		self.nikkor = LensBrand(
			lens_brand_name = "Nikkor"
			)

	def test_nikkor_is_instance_of_lens_brand(self):
		self.assertIsInstance(self.nikkor, LensBrand)

	def test_lens_brand_has_name(self):
		self.assertEqual("Nikkor", self.nikkor.lens_brand_name)