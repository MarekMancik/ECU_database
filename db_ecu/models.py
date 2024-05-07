from django.db import models


# Create your models here.
class ECU(models.Model):
    # family_name = models.CharField(max_length=20)
    ecu_name = models.CharField(max_length=20)
    customer_number = models.CharField(max_length=15)
    al_part_no = models.CharField(max_length=10, null=True, blank=True)
    hw_number = models.CharField(max_length=10)
    sw_number = models.CharField(max_length=10)
    ecu_comment = models.CharField(max_length=30)
    testing = models.CharField(max_length=5, blank=True)

    def __str__(self) -> str:
        return self.ecu_name
