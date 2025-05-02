from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Hotspot

class HotspotTests(APITestCase):
    def test_create_hotspot(self):
        url = reverse('hotspot-list-create')
        data = {
            'name': 'Central Park',
            'description': 'Great for warblers',
            'location_lat': 40.785091,
            'location_long': -73.968285
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_hotspots(self):
        Hotspot.objects.create(
            name='Lake View',
            location_lat=35.6895,
            location_long=139.6917
        )
        url = reverse('hotspot-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)