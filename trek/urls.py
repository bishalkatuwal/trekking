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
                #    MediaListView,
                   GuideListView,
                   GuideDetailsView, 
                   MaterialsView,
                   MaterialsDetailView,
                   AddtoCartView,
                   CartListView,
                   RemoveCartView,
                   success_view,
                   booking_success,
                   TripBookingView
                  
                  
)




urlpatterns = [


    path('book-trip/<int:pk>/', TripBookingView.as_view(), name='book_trip'),
    path('booking-success/', booking_success, name='booking_success'),
    path('contacts/success/', success_view, name='success'),   
    path('add-to-cart/', CartListView.as_view(), name = 'cart-list-view'),
    path('remove-cart/<int:materials_id>/', RemoveCartView.as_view(), name='remove-cart'),
    path('add-to-cart/<int:materials_id>/', AddtoCartView.as_view(), name='add-to-cart'),
    path('materials/<int:pk>/', MaterialsDetailView.as_view(), name='materials_detail'),
    path('materials/', MaterialsView.as_view(), name='materials'),  
    path('guide/<int:pk>/', GuideDetailsView.as_view(), name = 'guide_details'),
    path('guide/', GuideListView.as_view(), name = 'guide_list'),
    # path('trip-media/', MediaListView.as_view(), name='image_video'),
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