from django.http import request
from Core.models import SystemInformation
from SpareParts.models import *
from Machines.models import * 

def allcontext(request):
    info = SystemInformation.objects.filter(id=1)
    spare_parts = SparePartsNames.objects.filter(deleted=False)
    machines = MachinesNames.objects.filter(deleted=False)
    context = {
        'info':info,
        'spare_parts':spare_parts,
        'machines':machines,
    }
    return context