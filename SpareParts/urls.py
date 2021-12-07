from django.urls import path 
from .views import *

app_name = 'SpareParts'
urlpatterns = [
   # Spare Parts Type Module 
   path('sparepartsList/', SparePartsTypeList.as_view(), name="SpareTypeList" ),
   path('sparepartsTrachList/', SparePartsTypeTrachList.as_view(), name="SpareTypeTrachList" ),
   path('sparepartsType/create/', SparePartsTypeCreate.as_view(), name='SparePartsTypeCreate'),
   path('sparepartsType/<int:pk>/update/', SparePartsTypeUpdate.as_view(), name='SparePartsTypeUpdate'),
   path('sparepartsType/<int:pk>/delete/', SparePartsTypeDelete.as_view(), name='SparePartsTypeDelete'),
   path('sparepartsType/<int:pk>/restore/', SparePartsTypeRestore.as_view(), name='SparePartsTypeRestore'),
   #-------------------------------------------------------------------------------------------------------
   
   # Spare Parts Names Module 
   path('sparepartsNameList/', SparePartsNameList.as_view(), name="SparePartsNameList" ),
   path('sparepartsNameTrachList/', SparePartsNameTrachList.as_view(), name="SpareNameTrachList" ),
   path('sparepartsName/create/', SparePartsNameCreate.as_view(), name='SparePartsNameCreate'),
   path('sparepartsName/<int:pk>/update/', SparePartsNameUpdate.as_view(), name='SparePartsNameUpdate'),
   path('sparepartsName/<int:pk>/delete/', SparePartsNameDelete.as_view(), name='SparePartsNameDelete'),
   path('sparepartsName/<int:pk>/restore/', SparePartsNameRestore.as_view(), name='SparePartsNameRestore'),
   #-------------------------------------------------------------------------------------------------------
   
   
   # Spare Parts Warehouses Module 
   path('sparepartsWarehouseList/', SparePartsWarehouseList.as_view(), name="SparePartsWarehouseList" ),
   path('sparepartsWarehouseTrachList/', SparePartsWarehouseTrachList.as_view(), name="SparePartsWarehouseTrachList" ),
   path('sparepartsWarehouse/create/', SparePartsWarehouseCreate.as_view(), name='SparePartsWarehouseCreate'),
   path('sparepartsWarehouse/<int:pk>/update/', SparePartsWarehouseUpdate.as_view(), name='SparePartsWarehouseUpdate'),
   path('sparepartsWarehouse/<int:pk>/delete/', SparePartsWarehouseDelete.as_view(), name='SparePartsWarehouseDelete'),
   path('sparepartsWarehouse/<int:pk>/restore/', SparePartsWarehouseRestore.as_view(), name='SparePartsWarehouseRestore'),
   #-------------------------------------------------------------------------------------------------------
   
   
   # Spare Parts Supplier Module 
   path('sparepartsSupplierList/', SparePartsSupplierList.as_view(), name="SparePartsSupplierList" ),
   path('sparepartsSupplierTrachList/', SparePartsSupplierTrachList.as_view(), name="SparePartsSupplierTrachList" ),
   path('sparepartsSupplier/create/', SparePartsSupplierCreate.as_view(), name='SparePartsSupplierCreate'),
   path('sparepartsSupplier/<int:pk>/update/', SparePartsSupplierUpdate.as_view(), name='SparePartsSupplierUpdate'),
   path('sparepartsSupplier/<int:pk>/delete/', SparePartsSupplierDelete.as_view(), name='SparePartsSupplierDelete'),
   path('sparepartsSupplier/<int:pk>/restore/', SparePartsSupplierRestore.as_view(), name='SparePartsSupplierRestore'),
   #--------------------------------------------------------------------------------------------------------------------
   
   # Spare Parts Orders Module 
   path('sparepartsOrdersList/', SparePartsOrderList.as_view(), name="SparePartsOrderList" ),
   path('sparepartsOrder/create/', SparePartsOrderCreate.as_view(), name='SparePartsOrderCreate'),
   path('sparepartsOrder/<int:pk>/detail/', SparePartsOrderDetail, name='SparePartsOrderDetail'),
   path('sparepartsOrder/<int:pk>/update/', SparePartsOrderUpdate.as_view(), name='SparePartsOrderUpdate'),
   path('sparepartsOrderProduct/<int:pk>/create/', AddProductOrder, name='AddProductOrder'),
]
