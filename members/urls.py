from django.urls import path
from .views import RegisterView, ProfileDetailView, ProfileEditView,  BookingTripView,RemoveFromListView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register' ),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit', ProfileEditView.as_view(), name='profile-edit'),
    path('booking-list/<int:trip_id>/', BookingTripView.as_view(), name='booking_trip'),
    path('remove-from-list/<int:item_id>/', RemoveFromListView.as_view(), name='remove_from_list'),

]