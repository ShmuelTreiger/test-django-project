from django.db import models
from django.db.models import UniqueConstraint


class TestModel(models.Model):
    x = models.CharField(max_length=100)
    y = models.PositiveIntegerField(default=0)
    z = models.BooleanField(default=False, null=True)