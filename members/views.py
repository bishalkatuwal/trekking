from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views import generic
from django.views.generic import CreateView, DetailView,UpdateView, ListView
from .forms import SignupForm
from django.urls import reverse_lazy
from .models import Profile
from trek.models import  Trip, Materials, AddToCart
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

        return context



class ProfileEditView(UpdateView):
    models = Profile
    fields = ['bio', 'profile_pic']
    success_url = reverse_lazy('home')
    template_name = 'profile/profile_edit.html'

    def get_object(self, queryset=None):

        return self.request.user.profile





