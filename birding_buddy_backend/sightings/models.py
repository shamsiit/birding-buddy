from django.db import models
from users.models import CustomUser

class Sighting(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    species_name = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    behavior_notes = models.TextField(blank=True)
    photo = models.ImageField(upload_to='sightings/', blank=True, null=True)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)