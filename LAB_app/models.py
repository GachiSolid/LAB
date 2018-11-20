from django.db import models

class NProducts (models.Model):
    id = models.IntegerField()
    name = models.TextField()
    price = models.IntegerField()
    type = models.TextField()
    formFactor = models.ForeignKey(
        'Shipment', on_delete=models.CASCADE,
    )

class Shipment (models.Model):
    formFactor = models.TextField()
    method = models.TextField()

class HProducts (models.Model):
    id = models.IntegerField()
    name = models.TextField()
    price = models.IntegerField()
    cal = models.IntegerField()

class Contacts (models.Model):
    id = models.IntegerField()
    organization = models.TextField()
    post = models.TextField()
    phone = models.TextField()
    phone2 = models.TextField()
    email = models.TextField()