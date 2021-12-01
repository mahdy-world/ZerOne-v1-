from django.urls import path 
from .views import *

app_name = 'SpareParts'
urlpatterns = [
   path('spareparts/', SparePartsTypeList.as_view(), name="SpareTypeList" ),
   path('sparepartsName/', SparePartsNameList.as_view(), name="SpareNameList" )
]
