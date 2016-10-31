from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class ContactUs(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=40)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=254)
	reason = models.CharField(max_length=4, choices=(
			('op1', 'Exec Assistant'),
			('op2', 'Operational Review'),
			('op3', 'Other'),
		),default="op1")
	details = models.CharField(max_length=50)
	pub_date = models.DateTimeField(default=datetime.now)
	date_modified = models.DateTimeField(blank=True, null=True)


	def save(self):
		if self.id:
    			self.date_modified = datetime.now()
    		super(ContactUs, self).save()

	def __str__(self):
		return self.first_name + " " + self.last_name

