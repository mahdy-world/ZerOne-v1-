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
]   