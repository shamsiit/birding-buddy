from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser
from .models import Sighting

class SightingTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='sightuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_sighting(self):
        url = reverse('sighting-list-create')
        data = {
            'species_name': 'Sparrow',
            'count': 3,
            'behavior_notes': 'Feeding',
            'location_lat': 23.8103,
            'location_long': 90.4125,
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_list_sightings(self):
        Sighting.objects.create(
            user=self.user,
            species_name='Crow',
            count=2,
            location_lat=23.8103,
            location_long=90.4125
        )
        url = reverse('sighting-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)