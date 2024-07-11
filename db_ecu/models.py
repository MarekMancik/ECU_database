from django.db import models
from datetime import datetime

from django.db.models import CharField
from django.contrib.auth.models import User


# Create your models here.

class Family(models.Model):
    # Table model for Family ECU
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ECU(models.Model):
    # Table model for ECU
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True)
    ecu_name = models.CharField(max_length=20)
    customer_number = models.CharField(max_length=15)
    al_part_no = models.CharField(max_length=11, default='N/A',null=True, blank=True)
    hw_number = models.CharField(max_length=10)
    sw_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ecu_description = models.CharField(max_length=40, null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self) -> CharField:
        return self.ecu_name

    def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y at %I:%M %p')
