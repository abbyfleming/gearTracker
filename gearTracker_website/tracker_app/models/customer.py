from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
	"""
	Author: @abbyfleming
	
	Purpose: The Customer model will hold information to allow a customer to register for the website. It utilizes django's User class, but it set up in this way to allow future growth for the customer's fields.

	Properties: user - one to one field on User (first_name, last_name, email, username, password)
	
	Methods: __str__ Returns a customer's first and last name  
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return "{} {}".format(self.user.first_name, self.user.last_name)
