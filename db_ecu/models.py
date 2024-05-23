from django.db import models
from datetime import datetime


# Create your models here.
class ECU(models.Model):
    # family_name = models.CharField(max_length=20)
    ecu_name = models.CharField(max_length=20)
    customer_number = models.CharField(max_length=15)
    al_part_no = models.CharField(max_length=10, null=True, blank=True)
    hw_number = models.CharField(max_length=10)
    sw_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    ecu_comment = models.CharField(max_length=30)


    def __str__(self) -> str:
        return self.ecu_name

    def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y at %I:%M %p')
