from django.db import models
from django.contrib.auth.models import User


class DashboardCards(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    description = models.CharField(max_length=100, null=False)
    count = models.IntegerField(default=0, null=False)


class Challenges(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    type = models.IntegerField(null=False)
    level = models.IntegerField(null=False)
    modified_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)


class LeaderBoard(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    challenge = models.ForeignKey(Challenges, on_delete=models.CASCADE)
