from django.http import request
from Core.models import SystemInformation


def allcontext(request):
    info = SystemInformation.objects.filter(id=1)
    context = {
        'info':info
    }
    return context