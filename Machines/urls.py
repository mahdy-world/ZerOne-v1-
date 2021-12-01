from django.urls import path 
from .views import *

app_name = 'Machines'
urlpatterns = [
    path('types_active_list/', TypesActiveList.as_view(), name='types_active_list'),
    path('types_trash_list/', TypesTrashList.as_view(), name='types_trash_list'),
    path('types_create/', TypesCreate.as_view(), name='types_create')
]
