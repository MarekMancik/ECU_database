from django import forms
from db_ecu.models import ECU


class ECUForm(forms.ModelForm):
    class Meta:
        model = ECU
        fields = '__all__'
