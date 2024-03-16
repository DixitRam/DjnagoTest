from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


class Farm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name
    
class FarmDetails(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    weight = models.IntegerField()
    piece = models.IntegerField()
    abw = models.DecimalField(max_digits=10,decimal_places=3)
    gain = models.DecimalField(max_digits=10,decimal_places=3)
    adg = models.DecimalField(max_digits=10,decimal_places=3)
    date = models.DateField()

    
class WeatherReport(models.Model):
    temperature = models.DecimalField(max_digits=10,decimal_places=3)
    humidity = models.DecimalField(max_digits=10,decimal_places=3)
    wind_speed = models.DecimalField(max_digits=10,decimal_places=3)
    wind_direction = models.CharField(max_length=255)
    date = models.DateField()
