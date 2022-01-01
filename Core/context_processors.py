from django.http import request
from Core.models import SystemInformation
from SpareParts.models import *
from Machines.models import * 

def allcontext(request):
    info = SystemInformation.objects.filter(id=1)
    spare_parts = SparePartsNames.objects.filter(deleted=0)
    machines = MachinesNames.objects.filter(deleted=False)
    spare_order = SparePartsOrders.objects.filter(deleted=False)
    machine_order = MachinesOrders.objects.filter(deleted=False)
    context = {
        'info':info,
        'spare_parts':spare_parts,
        'machines':machines,
        'spare_order':spare_order,
        'machine_order':machine_order
    }
    return context