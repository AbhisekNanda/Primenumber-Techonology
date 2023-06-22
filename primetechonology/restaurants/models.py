from django.db import models

# Create your models here.
class Restaurant(models.Model):
    rest_id= models.IntegerField()
    rest_name = models.CharField(max_length=100)
    rest_location = models.CharField(max_length=100)
    rest_items = models.JSONField(null=True)
    rest_lat_long = models.CharField(max_length=100)
    rest_full_details = models.JSONField(null=True)


