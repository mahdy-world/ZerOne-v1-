from django.shortcuts import render

# Create your views here.

def TypesList(request):
    return render(request, 'types/types_list.html')