from django.shortcuts import render
from db_ecu.models import ECU
from django.forms import ModelForm
from collections import defaultdict


# Create your views here.
def ecu_tables(request):
    ecu_list = ECU.objects.select_related('family').all()
    families_ecus = defaultdict(list)
    for ecu in ecu_list:
        families_ecus[ecu.family.name].append(ecu)

    sorted_families_ecus = dict(sorted(families_ecus.items()))
    return render(request, 'ECU_tables.html', {'families_ecus': sorted_families_ecus})


class EcuForm(ModelForm):
    class Meta:
        model = ECU
        fields = "__all__"


def create_ecu(request):
    ecu_form = EcuForm()
    return render(request, 'create_ecu.html', {'ecu_form': ecu_form})
