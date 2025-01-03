from django import forms
from.models import Contact, Review, Booking

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','body']




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['trips', 'full_name', 'email', 'contact', 'emergency_contacts', 'participants', 
                  'country', 'arrival_date', 'departure_date', 'others_information']

        # Customizing widgets for date fields, and text fields
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),  # Date input for arrival date
            'departure_date': forms.DateInput(attrs={'type': 'date'}),  # Date input for departure date
            'emergency_contacts': forms.Textarea(attrs={'rows': 4, 'placeholder': 'List emergency contacts'}),
            'others_information': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Additional information'}),
        }

    # Custom Validation for contact number
    def clean_contact(self):
        contact = self.cleaned_data['contact']
        if not contact.isdigit() or len(contact) < 10:
            raise forms.ValidationError("Contact number must be numeric and at least 10 digits.")
        return contact

    # Custom Validation for emergency contacts
    def clean_emergency_contacts(self):
        emergency_contacts = self.cleaned_data['emergency_contacts']
        if not emergency_contacts:
            raise forms.ValidationError("Emergency contacts are required.")
        return emergency_contacts

    # Custom Validation for participants
    def clean_participants(self):
        participants = self.cleaned_data['participants']
        if participants <= 0:
            raise forms.ValidationError("The number of participants must be greater than 0.")
        return participants