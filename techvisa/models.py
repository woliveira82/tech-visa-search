from django.db import models

class Company(models.Model):
    tax_number = models.CharField(max_length=12)
    name = models.CharField(max_length=128)
    certification_date = models.DateField()
    expiration_date = models.DateField()
