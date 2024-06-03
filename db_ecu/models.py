from django.db import models
from datetime import datetime

from django.db.models import CharField


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
    al_part_no = models.CharField(max_length=10, null=True, blank=True)
    hw_number = models.CharField(max_length=10)
    sw_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    ecu_comment = models.CharField(max_length=30)

    def __str__(self) -> CharField:
        return self.ecu_name

    def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y at %I:%M %p')
