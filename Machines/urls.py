from django.urls import path 
from .views import *

app_name = 'Machines'
urlpatterns = [
    path('types_active_list/', TypesActiveList.as_view(), name='types_active_list'),
    path('types_trash_list/', TypesTrashList.as_view(), name='types_trash_list'),
    path('types_create/', TypesCreate.as_view(), name='types_create'),
    path('types_update/<int:pk>/edit/', TypesUpdate.as_view(), name='types_update'),
    path('types_delete/<int:pk>/edit/', TypesDelete.as_view(), name='types_delete'),
    path('types_restore/<int:pk>/restore/', TypesRestore.as_view(), name='types_restore'),
    path('types_super_delete/<int:pk>/super_delete/', TypesSuperDelete.as_view(), name='types_super_delete')
]
