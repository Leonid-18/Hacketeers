from django.conf import settings
from django.db import models


class Node(models.Model):
    custom_id = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    data = models.CharField(max_length=100000, null=True)


class Edge(models.Model):
    custom_id = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    target = models.SmallIntegerField(null=True, blank=True)
    source = models.SmallIntegerField(null=True, blank=True)
    data = models.CharField(max_length=100000, null=True)
