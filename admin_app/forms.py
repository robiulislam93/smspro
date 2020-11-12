from .models import Product,User
from django import forms

class AddProduct (forms.ModelForm):
       class Meta:
         model= Product
         fields ='__all__'
         widgets = {
             'name':forms.TextInput(attrs={'class':'form-control'}),
             'price':forms.TextInput(attrs={'class':'form-control'})

         }

class AddUser (forms.ModelForm):
       class Meta:
         model= User
         fields =['username','email','password','userstatus','User_type']
         widgets = {
             'username':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.TextInput(attrs={'class':'form-control'}),
             'password':forms.TextInput(attrs={'class':'form-control'}),
             'userstatus':forms.TextInput(attrs={'class':'form-control'}),
             'User_type':forms.TextInput(attrs={'class':'form-control'})
         }
        

