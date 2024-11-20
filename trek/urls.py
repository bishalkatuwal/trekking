from django.urls import path
# from.views import home_view


from.views import ContactView, TripDetailView ,PageDetailView ,PageView ,TraveInfoDetailView ,HomeView ,BlogView, TraveInfoView ,BlogDetailView, AddReviewView,AboutUsView ,ReviewView, TripsView




urlpatterns = [

    # path('',home_view, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('contatc/', ContactView.as_view(), name='contact-page'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('review/', AddReviewView.as_view(), name='review'),
    path('review/view/', ReviewView.as_view(), name='review-view'),
    path('about_us/', AboutUsView.as_view(), name='about'),
    path('travel/', TraveInfoView.as_view(), name='travel'),
    path('travel/detail<int:pk>',TraveInfoDetailView.as_view(), name='travel-detail' ),
    path('page/', PageView.as_view(), name='page'),
    path('trip/<int:pk>/',TripDetailView.as_view(), name='trip-detail'),


    path('trips/', TripsView.as_view(), name='trips'),

    path('<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
    
    
  
 

]