from django import forms
from django.core.exceptions import ValidationError

from .models import ContactUs

class ContactUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = ('first_name','last_name','phone','email','reason','details',)