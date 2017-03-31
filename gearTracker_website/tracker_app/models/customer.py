from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
	'''
	Purpose: 
		The Customer model defines the structure of a customer and utilizes Django's User model. 

	Properties: 
		user - OneToOneFieldfield on User (first_name, last_name, email, username, password)
	
	Methods:
		__str__ Returns user.first_name, user.last_name (ie: Suzy Bishop)
	'''

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return "{} {}".format(self.user.first_name, self.user.last_name)
