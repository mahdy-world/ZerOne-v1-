from django.urls import path
from .views import *

app_name = "Auth"
urlpatterns = [
    path('users/login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('ChangePassword/', ChangePassword, name='ChangePassword'),

]