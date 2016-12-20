from django.forms import ModelForm
from django import forms
from .models import Order
from .models import Product_Category

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['Name','PhoneNo','Emailid','Product']
        widgets={
                 'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
                 'PhoneNo':forms.TextInput(attrs={'class':'form-control','placeholder':'Mob.No'}),
                 'Emailid':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
                 }