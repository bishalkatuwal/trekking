from django import forms
from.models import Contact, Review

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','body']