from django.urls import path
# from.views import home_view


from.views import ( ContactView ,
                    TripDetailView ,
                    TripCategoryListView, 
                    TripCategoryDetailView,
                    PageDetailView,
                    PageView,
                    TraveInfoDetailView,
                    HomeView,
                    BlogView,
                    TraveInfoView,
                    BlogDetailView,
                    AddReviewView,
                    ReviewView,
                   MediaListView
)




urlpatterns = [

   # Trip Booking List
    
    path('trip-media/', MediaListView.as_view(), name='image_video'),
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact-page'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('review/', AddReviewView.as_view(), name='review'),
    path('review/view/', ReviewView.as_view(), name='review-view'),
    path('travel/', TraveInfoView.as_view(), name='travel'),
    path('travel/detail<int:pk>',TraveInfoDetailView.as_view(), name='travel-detail' ),
    path('page/', PageView.as_view(), name='page'),
    
    path('trips/<slug:slug>/', TripDetailView.as_view(), name='trip_detail'),
    path('trip-category/<slug:slug>/', TripCategoryDetailView.as_view(), name='trip_category_detail'),
    path('trip-categories/', TripCategoryListView.as_view(), name='trip_category_list'),


    
    path('<slug:slug>/', PageDetailView.as_view(), name='page_detail'),

]