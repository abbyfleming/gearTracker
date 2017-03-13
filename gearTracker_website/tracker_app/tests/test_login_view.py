from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from tracker_app.views import login_view

import sys 
sys.path.append('../')  




class TestLogin(TestCase):
	"""
	Purpose: This class tests matters related to Login
	Methods:
	Author: Abby
	"""
