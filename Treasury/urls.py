from django.urls import path 
from .views import *

app_name = 'Treasury'
urlpatterns = [
   
   path('WorkTreasuryList/', WorkTreasuryList.as_view(), name="WorkTreasuryList" ),
   path('WorkTreasuryListTrachList/', WorkTreasuryTrachList.as_view(), name="WorkTreasuryTrachList" ),
   path('WorkTreasury/create/', WorkTreasuryCreate.as_view(), name='WorkTreasuryCreate'),
   path('WorkTreasuryCreate/<int:pk>/update/', WorkTreasuryUpdate.as_view(), name='WorkTreasuryUpdate'),
   path('WorkTreasury/<int:pk>/delete/', WorkTreasuryDelete.as_view(), name='WorkTreasuryDelete'),
   path('WorkTreasury/<int:pk>/restore/', WorkTreasuryRestore.as_view(), name='WorkTreasuryRestore'),
   path('WorkTreasury/<int:pk>/super_delete/', WorkTreasurySuperDelete.as_view(), name='WorkTreasurySuperDelete'),
   #-------------------------------------------------------------------------------------------------------
   
   
   path('HomeTreasuryList/', HomeTreasuryList.as_view(), name="HomeTreasuryList" ),
   path('HomeTreasuryListTrachList/', HomeTreasuryTrachList.as_view(), name="HomeTreasuryTrachList" ),
   path('HomeTreasury/create/', HomeTreasuryCreate.as_view(), name='HomeTreasuryCreate'),
   path('HomeTreasuryCreate/<int:pk>/update/', HomeTreasuryUpdate.as_view(), name='HomeTreasuryUpdate'),
   path('HomeTreasury/<int:pk>/delete/', HomeTreasuryDelete.as_view(), name='HomeTreasuryDelete'),
   path('HomeTreasury/<int:pk>/restore/', HomeTreasuryRestore.as_view(), name='HomeTreasuryRestore'),
   path('HomeTreasury/<int:pk>/super_delete/', HomeTreasurySuperDelete.as_view(), name='HomeTreasurySuperDelete'),
   #-------------------------------------------------------------------------------------------------------
   
   
   
   path('BankAccountList/', BankAccountList.as_view(), name="BankAccountList" ),
   path('BankAccountListTrachList/', BankAccountTrachList.as_view(), name="BankAccountTrachList" ),
   path('BankAccount/create/', BankAccountCreate.as_view(), name='BankAccountCreate'),
   path('BankAccountCreate/<int:pk>/update/', BankAccountUpdate.as_view(), name='BankAccountUpdate'),
   path('BankAccount/<int:pk>/delete/', BankAccountDelete.as_view(), name='BankAccountDelete'),
   path('BankAccount/<int:pk>/restore/', BankAccountRestore.as_view(), name='BankAccountRestore'),
   path('BankAccount/<int:pk>/super_delete/', BankAccountSuperDelete.as_view(), name='BankAccountSuperDelete'),
   #-------------------------------------------------------------------------------------------------------
]   