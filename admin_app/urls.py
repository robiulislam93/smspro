from django.urls import path
from .views import *

urlpatterns = [
    
    path('userlist', show_user),
    path('profile/<id>', show_profile,name='profile'),
    path('addproduct', add_product,name='addproduct'),
    path('adduser',add_user,name='adduser'),

    

]