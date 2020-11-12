from .models import Dokan
from django import forms
from django.contrib.auth.models import User

#class AddProduct (forms.ModelForm):
   #    class Meta:
    #     model= Product
      #   fields ='__all__'
        # widgets = {
         #    'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'price':forms.TextInput(attrs={'class':'form-control'})

        # }

class UserForm (forms.ModelForm):
       class Meta:
         model= User
         fields =['username','password']
         help_texts={
             'username':None
         }
         
         
         widgets = {
             'username':forms.TextInput(attrs={'class':'form-control'}),
             'password':forms.PasswordInput(attrs={'class':'form-control'})
          #   'email':forms.TextInput(attrs={'class':'form-control'}),
           #  'password':forms.TextInput(attrs={'class':'form-control'}),
            # 'userstatus':forms.TextInput(attrs={'class':'form-control'}),
            # 'User_type':forms.TextInput(attrs={'class':'form-control'})
         }
        

