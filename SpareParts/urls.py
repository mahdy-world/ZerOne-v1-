from django.urls import path 
from .views import *

app_name = 'SpareParts'
urlpatterns = [
   path('sparepartsList/', SparePartsTypeList.as_view(), name="SpareTypeList" ),
   path('sparepartsType/create/', SparePartsTypeCreate.as_view(), name='SparePartsTypeCreate'),
   path('sparepartsType/<int:pk>/update/', SparePartsTypeUpdate.as_view(), name='SparePartsTypeUpdate'),

]
