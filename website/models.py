from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class ContactUs(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=40)
	company_name = models.CharField(max_length=125, blank=True)
	website = models.CharField(max_length=125, blank=True)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=254)
	service = models.CharField(max_length=4, choices=(
			('op1', 'Consultation'),
			('op2', 'Administrative Assistance'),
			('op3', 'Other'),
		),default="op1")
	brief_description = models.TextField(max_length=500)
	how_did_you_hear_about_us = models.CharField(max_length=4, choices=(
		('op1', 'Word of Mouth'),
		('op2', 'Facebook'),
		('op3', 'Google Search'),
		('op4', 'Other'),
	),default="op1")
	pub_date = models.DateTimeField(default=datetime.now)
	date_modified = models.DateTimeField(blank=True, null=True)

	def save(self):
		if self.id:
			self.date_modified = datetime.now()
			super(ContactUs, self).save()

	def __str__(self):
		return self.first_name + " " + self.last_name


class ContentManagement(models.Model):
	cm_title = models.CharField(max_length=50)
	cm_philosophy = models.TextField()
	cm_about_us = models.TextField()
	cm_team_para_one = models.TextField()
	cm_team_para_two = models.TextField()
	cm_service_admin = models.TextField()
	cm_service_consultation = models.TextField()
	cm_date_modified = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.cm_title

class ContactStatus(models.Model):
	contact_id = models.ForeignKey(ContactUs, on_delete=models.CASCADE)
	followup_completed = models.BooleanField(blank=True)
	date_completed = models.DateTimeField(blank=True, null=True)
	notes = models.TextField(max_length=500)
	priority = models.IntegerField()

	def save(self):
		super(ContactStatus, self).save()
		
	def __str__(self):
		return self.contact_id.first_name + " " + self.contact_id.first_name

		