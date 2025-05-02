from django.db import models

class Hotspot(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)