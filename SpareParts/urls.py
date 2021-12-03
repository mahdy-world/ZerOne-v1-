from django.urls import path 
from .views import *

app_name = 'SpareParts'
urlpatterns = [
   # Spare Type Module 
   path('sparepartsList/', SparePartsTypeList.as_view(), name="SpareTypeList" ),
   path('sparepartsTrachList/', SparePartsTypeTrachList.as_view(), name="SpareTypeTrachList" ),
   path('sparepartsType/create/', SparePartsTypeCreate.as_view(), name='SparePartsTypeCreate'),
   path('sparepartsType/<int:pk>/update/', SparePartsTypeUpdate.as_view(), name='SparePartsTypeUpdate'),
   path('sparepartsType/<int:pk>/delete/', SparePartsTypeDelete.as_view(), name='SparePartsTypeDelete'),
   path('sparepartsType/<int:pk>/restore/', SparePartsTypeRestore.as_view(), name='SparePartsTypeRestore'),
   #-------------------------------------------------------------------------------------------------------
   
   # Spare Type Module 
   path('sparepartsNameList/', SparePartsNameList.as_view(), name="SparePartsNameList" ),
   path('sparepartsNameTrachList/', SparePartsNameTrachList.as_view(), name="SpareNameTrachList" ),
   path('sparepartsName/create/', SparePartsNameCreate.as_view(), name='SparePartsNameCreate'),
   path('sparepartsName/<int:pk>/update/', SparePartsNameUpdate.as_view(), name='SparePartsNameUpdate'),
   path('sparepartsName/<int:pk>/delete/', SparePartsNameDelete.as_view(), name='SparePartsNameDelete'),
   path('sparepartsName/<int:pk>/restore/', SparePartsNameRestore.as_view(), name='SparePartsNameRestore'),
   #-------------------------------------------------------------------------------------------------------
]
