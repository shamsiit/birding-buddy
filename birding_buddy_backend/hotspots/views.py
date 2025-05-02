from rest_framework import generics
from .models import Hotspot
from .serializers import HotspotSerializer

class HotspotListCreateView(generics.ListCreateAPIView):
    queryset = Hotspot.objects.all()
    serializer_class = HotspotSerializer

class HotspotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotspot.objects.all()
    serializer_class = HotspotSerializer