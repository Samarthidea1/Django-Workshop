from django.db import models

class Items(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)