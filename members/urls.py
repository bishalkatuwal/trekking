from django.urls import path
from .views import RegisterView, ProfileDetailView, ProfileEditView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register' ),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit', ProfileEditView.as_view(), name='profile-edit')

]