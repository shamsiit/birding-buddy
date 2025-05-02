from rest_framework import generics, permissions
from .models import Sighting
from .serializers import SightingSerializer

class SightingListCreateView(generics.ListCreateAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SightingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
    permission_classes = [permissions.IsAuthenticated]