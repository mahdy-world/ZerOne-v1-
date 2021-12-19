from django.urls import path 
from . import views

app_name = 'Core'
urlpatterns = [
    path('', views.Index, name='index'),
    path('systemInfoCreate/', views.SystemInfoCreate.as_view(), name='SystemInfoCreate'),
    path('systemInfoUpdate/<int:pk>', views.SystemInfoUpdate.as_view(), name='SystemInfoUpdate')
]
