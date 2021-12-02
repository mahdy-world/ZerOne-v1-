from django.urls import path 
from .views import *

app_name = 'SpareParts'
urlpatterns = [
   path('sparepartsList/', SparePartsTypeList.as_view(), name="SpareTypeList" ),
   path('sparepartsTrachList/', SparePartsTypeTrachList.as_view(), name="SpareTypeTrachList" ),
   path('sparepartsType/create/', SparePartsTypeCreate.as_view(), name='SparePartsTypeCreate'),
   path('sparepartsType/<int:pk>/update/', SparePartsTypeUpdate.as_view(), name='SparePartsTypeUpdate'),
   path('sparepartsType/<int:pk>/delete/', SparePartsTypeDelete.as_view(), name='SparePartsTypeDelete'),
   path('sparepartsType/<int:pk>/restore/', SparePartsTypeRestore.as_view(), name='SparePartsTypeRestore'),

]
