from django.shortcuts import render
from .forms import ECUForm
from django.http import HttpResponseRedirect


# Create your views here.
def add_ecu(request):
    if request.method == "POST":
        form = ECUForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ECU-tables/')
        else:
            form = ECUForm()
        return render(request, 'ECU_tables.html', {'form': form})
