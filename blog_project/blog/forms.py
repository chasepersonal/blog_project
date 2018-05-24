# Import library to allow form creation

from django import forms
from .models import Post

# Class for contact form

class ContactForm(forms.Form):
    contact_name = forms.CharField(
        max_length=75,
        label='Your full name')
    contact_email = forms.EmailField(
        max_length=300,
        label='Your e-mail address')
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=3000,)

	# Clean data to allow for custom validation messages

    def clean(self):
		cleaned_data = super(ContactForm, self).clean()
		contact_name = cleaned_data.get('contact_name')
		contact_email = cleaned_data.get('contact_email')
		message = cleaned_data.get('message')
		
		# If all fields do not have a value, raise a custom validation message
		
		if not contact_name and not contact_email and not message:
    			raise forms.ValidationError('You have to fill out all fields!')

        


