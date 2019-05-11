from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    level = models.IntegerField()
    awards = models.CharField(max_length=255)


class Sardana(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()
    first_compass_position = models.DecimalField(max_digits=6, decimal_places=3)
    number_curts = models.IntegerField()
    number_llargs = models.IntegerField()
    beats_per_minute_curts = models.DecimalField(max_digits=5, decimal_places=2)
    beats_per_minute_llargs = models.DecimalField(max_digits=5, decimal_places=2)
