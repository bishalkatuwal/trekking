from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views import generic
from django.views.generic import CreateView, DetailView,UpdateView, ListView
from .forms import SignupForm
from django.urls import reverse_lazy
from .models import Profile
from trek.models import TripBooking, Trip, Materials, AddToCart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages

class RegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url  = reverse_lazy('login')




class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # This ensures that the logged-in user has a profile, or creates one if it doesn't exist
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the trip booking list for the logged-in user to the context
        context['tripbooking_list'] = TripBooking.objects.filter(user=self.request.user)

        return context



class ProfileEditView(UpdateView):
    models = Profile
    fields = ['bio', 'profile_pic']
    success_url = reverse_lazy('home')
    template_name = 'profile/profile_edit.html'

    def get_object(self, queryset=None):

        return self.request.user.profile




class BookingTripView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        trip = get_object_or_404(Trip, id=self.kwargs['trip_id'])

        # Check if the trip is already booked by the user
        if TripBooking.objects.filter(user=request.user, trip=trip).exists():
            messages.info(request, "This trip is already in your list.")
        else:
            # Create a new TripBooking object
            TripBooking.objects.create(user=request.user, trip=trip)
            messages.success(request, f"'{trip.title}' has been added to your booking list.")

        # Redirect to the trip booking list
        return redirect('profile-detail')


class TripBookingListView(LoginRequiredMixin, ListView):
    model = TripBooking
    template_name = 'profile_detail.html'
    context_object_name = 'tripbooking_list'  # Makes template variable names consistent

    def get_queryset(self):
        """
        Returns a filtered queryset to display only the trips booked by the logged-in user.
        """
        return TripBooking.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Additional context can be added here if needed
        return context



class RemoveFromListView(View):
    def post(self, request, item_id):
        tripbooking_item = get_object_or_404(TripBooking, id=item_id)
        tripbooking_item.delete()
        return redirect('profile-detail')


