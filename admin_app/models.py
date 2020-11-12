from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=250)
    email= models.CharField(max_length=250,blank=True,null=True)
    password=models.CharField(max_length=50)
    userstatus=models.CharField(max_length=10)
    User_type= models.CharField(max_length=250,blank=True,null=True)
    action_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Product(models.Model):
    name= models.CharField(max_length=250)
    price= models.CharField(max_length=250)   

    def __str__(self):
        return self.name

