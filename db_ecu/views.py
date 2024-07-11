from django.shortcuts import render,get_object_or_404, redirect
from db_ecu.models import ECU
from django.forms import ModelForm
from collections import defaultdict
from django.contrib.auth.decorators import login_required


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
        fields = ['ecu_name', 'customer_number', 'hw_number', 'sw_number', 'ecu_description', 'comment']


@login_required
def create_ecu(request):
    ecu_form = EcuForm()
    return render(request, 'create_ecu.html', {'ecu_form': ecu_form})

@login_required
def edit_ecu(request, ecu_id):
    ecu_unit = get_object_or_404(ECU, id=ecu_id)

    # checking user
    if request.user != ecu_unit.creator:
        return redirect('You are not the ecus own - you can not change it!')



