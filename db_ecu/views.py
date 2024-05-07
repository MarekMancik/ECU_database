from django.shortcuts import render
from db_ecu.models import ECU
from django.forms import ModelForm



# Create your views here.
def ecu_tables(request):
    ecu_data = ECU.objects.all()
    ecu_name = ECU.ecu_name
    return render(request, 'ECU_tables.html', {'ecu_data': ecu_data, 'ecu_name': ecu_name})


class EcuForm(ModelForm):
    class Meta:
        model = ECU
        fields = "__all__"


def create_ecu(request):
    ecu_form = EcuForm()
    return render(request, 'create_ecu.html', {'ecu_form': ecu_form})


