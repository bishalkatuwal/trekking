from django.shortcuts import render, get_list_or_404,get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .forms import ContactForm, ReviewForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Contact, Blog, Review,  TravelInfo, Trip, Page, TripCategory , AddToCart, Materials, TripMedia, BlogMedia, Guide, Language
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
        context['trips'] = Trip.objects.all()[:2]
        context['categories'] = TripCategory.objects. select_related('trip','categories').all()
        context['pages'] = Page.objects.all()  
        context['blogs'] = Blog.objects.all()    
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
        blog = self.object  # Use the object retrieved by DetailView
        blog_media = BlogMedia.objects.filter(blog=blog)  # Fetch related BlogMedia
        context['blogs'] = blog_media
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
    template_name = 'trips_details.html'
    context_object_name = 'trip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the media related to this trip
        trip = self.object  # Get the current trip instance
        media = TripMedia.objects.filter(trip=trip)  # Get related media
        context['media'] = media  # Add media to context
        return context





class MediaListView(ListView):
    model = TripMedia
    template_name = 'trip_media.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TripMedia,self).get_context_data(*args, **kwargs)
        return context




class GuideListView(ListView):
    model = Guide
    template_name = 'Guide.html'
    

    def get_context_data(self, *args, **kwargs):
        context  =super().get_context_data( *args, **kwargs)
        return context


class GuideDetailsView(DetailView):
    model = Guide
    template_name = 'Guide_details.html'
    

    def get_context_data(self, *args, **kwargs):
        context  =super().get_context_data( *args, **kwargs)
        travel = get_object_or_404(Guide, id=self.kwargs['pk'])
        return context
    

class MaterialsView(ListView):
    model = Materials
    template_name = 'materials.html'

    def get_context_data(self, *args, **kwargs):
        context  =super().get_context_data( *args, **kwargs)
        return context



class MaterialsDetailView(DetailView):
    model = Materials
    template_name = 'materials_detail.html'


    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        materials = get_object_or_404(Materials, id=self.kwargs['pk'])

        return context






class AddtoCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        materials = get_object_or_404(Materials, id=self.kwargs['materials_id'])

        if AddToCart.objects.filter(user=request.user, materials=materials).exists():
            messages.info(request, "The item has already been added to your cart!")
        else:
            AddToCart.objects.create(user=request.user, materials=materials)
            messages.success(request, "This item has been added to your cart!")

        # Redirect to the user's profile page
        return redirect('cart-list-view')







class CartListView(ListView, LoginRequiredMixin):
    model = AddToCart
    template_name = 'add-to-cart.html'
    context_object_name = 'AddToCart_list'

    def get_queryset(self):
        # Filter cart items for the logged-in user
        return AddToCart.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional information, such as the total price of items in the cart
        total_price = sum(item.materials.price for item in context['AddToCart_list'])
        context['total_price'] = total_price
        return context


class RemoveCartView(View):
    def post(self, request, materials_id):
        # Fetch the AddToCart item associated with the user and the materials_id
        cart_item = get_object_or_404(AddToCart, materials__id=materials_id, user=request.user)
        
        # Delete the item from the cart
        cart_item.delete()
        
        # Optionally, add a success message
        messages.success(request, "Item removed from your cart.")

        # Redirect the user to a success page (you can adjust this to your desired page)
        return HttpResponseRedirect(reverse_lazy('cart-list-view'))
       




    