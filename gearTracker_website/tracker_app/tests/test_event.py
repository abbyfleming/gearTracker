from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from tracker_app.models.event import Event
import datetime

# python manage.py test tracker_app

class TestEvent(TestCase):
	"""
	Purpose: Test Events
	Author: Abby
	Tests: 
		
	"""

	@classmethod
	def setUpTestData(self):
		
		self.wedding = Event(
			name = "Wedding"
			)


	def test_wedding_is_instance_of_event(self):
		self.assertIsInstance(self.wedding, Event)
	
	def test_event_has_name(self):
		self.assertEqual("Wedding", self.wedding.name)

	

	