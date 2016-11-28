from django import forms
from django.core.exceptions import ValidationError

from .models import ContactUs
from .models import ContactStatus

class ContactUsForm(forms.ModelForm):
	class Meta:
		brief_description = forms.CharField(widget=forms.Textarea)
		model = ContactUs
		#details = forms.CharField (maxlength = 250)
		
		fields = ('first_name','last_name','company_name','website','phone','email','service','brief_description','how_did_you_hear_about_us',)

		#details = forms.CharField(required = False, widget=forms.Textarea)

class ContactStatusForm(forms.ModelForm):
	class Meta:
		model = ContactStatus
		fields = ('contact_id', 'followup_completed', 'date_completed', 'notes', 'priority',)
		