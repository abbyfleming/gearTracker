from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from tracker_app.models.customer import Customer
import datetime

# python manage.py test tracker_app

class TestCustomer(TestCase):
	"""
	Purpose: Test Customer
	Author: Abby
	Tests: 
		test_customer_is_instance
		test_customer_has_full_name
		test_customer_has_email
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


	def test_suzy_is_instance_of_customer(self):
		self.assertIsInstance(self.suzy, Customer)
	
	def test_customer_has_full_name(self):
		self.assertEqual("Suzy Bishop", self.user.first_name + " " + self.user.last_name)

	def test_customer_has_email(self):
		self.assertEqual("s@s.com", self.user.email)
	

	