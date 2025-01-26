from django import forms
from.models import Contact, Review, TripBooking, Trips_review

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','body']


# Trips Booking Form

class TripBookingForm(forms.ModelForm):
    class Meta:
        model = TripBooking
        fields = [
            'trips', 'trip_start_date', 'full_name', 'email_address',
            'country', 'contact_number', 'emergency_number',
            'flight_arrival_date', 'flight_departure_date', 'others_informations'
        ]
        widgets = {
            'trip_start_date': forms.DateInput(attrs={'type': 'date'}),
            'flight_arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'flight_departure_date': forms.DateInput(attrs={'type': 'date'}),
            'others_informations': forms.Textarea(attrs={'rows': 4}),
        }



class TripsReviewForm(forms.ModelForm):
    class Meta:
        model = Trips_review
        fields = ['rating', 'review']
        