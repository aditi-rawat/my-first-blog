from django.forms import ModelForm
from django import forms
from .models import customer


class customerForm(forms.ModelForm):
	class meta:
		model=customer
		fields=['name', 'contact']

		name=forms.CharField()
		contact=forms.CharField()
	
	
