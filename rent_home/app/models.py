from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import date

class Owner(User):
	status = models.BooleanField(default=True)

class HomeAssests(models.Model):
	name = models.CharField(max_length=50, default='')
	availabilty = models.BooleanField(default=True)
	rate_per_day = models.IntegerField(default=None)
	location = models.CharField(max_length=50, default='') 
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

class Renter(User):
	status = models.BooleanField(default=True)	

class Bookings(User):
	home = models.ForeignKey(HomeAssests, on_delete=models.CASCADE,blank=True)
	date_of_booking = models.DateField(default=date.today) 
	renter_person = models.ForeignKey(Renter, on_delete=models.CASCADE,blank=True)



