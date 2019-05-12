from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    level = models.IntegerField()
    awards = models.CharField(max_length=255)

