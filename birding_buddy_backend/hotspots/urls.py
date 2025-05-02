from django.urls import path
from .views import HotspotListCreateView, HotspotDetailView

urlpatterns = [
    path('', HotspotListCreateView.as_view(), name='hotspot-list-create'),
    path('<int:pk>/', HotspotDetailView.as_view(), name='hotspot-detail'),
]