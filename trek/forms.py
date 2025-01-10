from django import forms
from.models import Contact, Review, TripsBooking

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','body']


# Trips Booking Form


class TripsBookingForm(forms.ModelForm):
    class Meta:
        model = TripsBooking
        fields = ['trips', 'full_name', 'email', 'contact', 'emergency_contacts', 'participants', 
                  'country', 'arrival_date', 'departure_date', 'others_information']

