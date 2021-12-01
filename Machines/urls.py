from django.urls import path 
from . import views

app_name = 'Machines'
urlpatterns = [
    path('types_list/', views.TypesList, name='types_list')
]
