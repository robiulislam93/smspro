from django.urls import path
from .views import *

urlpatterns = [
    
    path('dokan', show_dokan),
    path('regi', user_create,name='regi'),
    path('login', user_login,name='login'),
    path('logout', user_logout,name='logout'),


]