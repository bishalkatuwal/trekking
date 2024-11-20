from django.shortcuts import render, get_list_or_404,get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from .forms import ContactForm, ReviewForm
from django.urls import reverse_lazy
from.models import Contact, Blog, Review, AboutUs, TravelInfo, Trip, Page, TripCategory




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





class TripsView(ListView):
    model = Trip
    template_name = 'trips.html'

    def get_context_data(self, *args, **kwargs):
       context = super(TripsView, self).get_context_data(*args, **kwargs)
    #    trips = get_list_or_404(TripsView, id=self.kwargs['pk'])
       return context


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip_detail.html'


    def get_queryset(self):
        
        # Exclude trips with no primary key or any other condition
        return Trip.objects.exclude(pk=None)


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
