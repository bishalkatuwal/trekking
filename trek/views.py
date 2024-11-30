from django.shortcuts import render, get_list_or_404,get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView
from .forms import ContactForm, ReviewForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Contact, Blog, Review, AboutUs, TravelInfo, Trip, Page, TripCategory , TripBooking
from django.contrib import messages



# def home_view(request):
#     return render(request, 'home.html')


class HomeView(ListView):
    model = TravelInfo  # This is the model you're displaying in the homepage
    template_name = 'home.html'
    context_object_name = 'travel_info'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add other context data here
        context['trip'] = Trip.objects.all()
        context['categories'] = TripCategory.objects. select_related('trip','destination').all()
        context['pages'] = Page.objects.all()         
        return context

    def get_queryset(self):
        # Customize your queryset for TravelInfo if needed
        return TravelInfo.objects.all()  # This will fetch all the TravelInfo items



class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        blog = get_object_or_404(Blog, id= self.kwargs['pk'])
        return context



class AddReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review.html'
    success_url = reverse_lazy('review-view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  



class ReviewView(ListView):
    model = Review
    template_name = 'review_view.html'

    def get_context_data(self, *args, **kwargs):
        context  =super(ReviewView,self).get_context_data( *args, **kwargs)
        return context



class AboutUsView(ListView):
    model = AboutUs
    template_name = 'aboutus.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutUsView, self).get_context_data( *args, **kwargs)
        return context




class TraveInfoView(ListView):
    model = TravelInfo
    template_name = 'travelinfo.html'

    def get_context_data(self, *args , **kwargs):
        context = super(TraveInfoView,self).get_context_data(*args, **kwargs)
        return context



class TraveInfoDetailView(DetailView):
    model = TravelInfo
    template_name = 'travel_detail.html'

    def get_context_data(self, *args , **kwargs):
        context = super(TraveInfoDetailView,self).get_context_data(*args, **kwargs)
        travel = get_object_or_404(TravelInfo, id=self.kwargs['pk'])
        return context






class PageView(ListView):
    model = Page
    template_name = 'page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PageView,self).get_context_data(*args, **kwargs)
        return context



class PageDetailView(DetailView):
    model = Page
    template_name = 'page_detail.html'
    context_object_name = 'page'

    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(Page, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['children'] = self.object.child_pages.all()  # Pass child pages to the template
        return context


class TripCategoryListView(ListView):
    model = TripCategory
    template_name = 'trip_category.html'  # Template for the trip category list
    context_object_name = 'categories'


class TripCategoryDetailView(DetailView):
    model = TripCategory
    template_name = 'trip_category_detail.html'  # Template for trips under a category
    context_object_name = 'trip_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get trips associated with this category
        context['trips'] = Trip.objects.filter(trip_category=self.object)
        return context


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trips_details.html'  # Create this template for trip details
    context_object_name = 'trip' 




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
        return redirect('tripbook_list')


class TripBookingListView(LoginRequiredMixin, ListView):
    model = TripBooking
    template_name = 'Tripbooking_list.html'
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







