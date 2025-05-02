from django.urls import path
from .views import UserProfileView, RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('<int:pk>/', UserProfileView.as_view(), name='user-profile'),
]