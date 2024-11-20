from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, DetailView,UpdateView
from .forms import SignupForm
from django.urls import reverse_lazy
from .models import Profile

class RegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url  = reverse_lazy('login')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'

    
    def get_object(self, queryset=None):
       profile, created = Profile.objects.get_or_create(user=self.request.user)
       return profile


class ProfileEditView(UpdateView):
    models = Profile
    fields = ['bio', 'profile_pic']
    success_url = reverse_lazy('home')
    template_name = 'profile/profile_edit.html'

    def get_object(self, queryset=None):

        return self.request.user.profile
