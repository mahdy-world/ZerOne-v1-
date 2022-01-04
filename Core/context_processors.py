import datetime
from django.http import request
from Core.models import SystemInformation
from SpareParts.models import *
from Machines.models import * 
from django.utils import timezone as tz
from django.db.models import Q



def allcontext(request):
    info = SystemInformation.objects.filter(id=1)
    spare_parts = SparePartsNames.objects.filter(deleted=0)
    machines = MachinesNames.objects.filter(deleted=False)
    spare_order = SparePartsOrders.objects.filter(deleted=False)
    machine_order = MachinesOrders.objects.filter(deleted=False)
    
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    
    notfaiy = MachineNotifecation.objects.filter(Q(created_at=tomorrow) | Q(created_at = today ) )
    notification_count = MachineNotifecation.objects.filter(Q(created_at=tomorrow) | Q(created_at = today ), read=False ).count()

    context = { 
        'info':info,
        'spare_parts':spare_parts,
        'machines':machines,
        'spare_order':spare_order,
        'machine_order':machine_order,
        'notifay':notfaiy,
        'today': today,
        'tomorrow' : tomorrow,
        'notification_count': notification_count

    }
    return context