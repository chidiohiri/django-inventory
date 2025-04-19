from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    restock_alert = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Outgoing(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_remaining = models.PositiveIntegerField(default=0)
    quantity_given = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Incoming(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_remaining = models.PositiveIntegerField(default=0)
    quantity_received = models.PositiveIntegerField(default=0)
    vendor = models.CharField(max_length=100, null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)