from django import forms
from .models import Sitter, Baby, Arrival, Departure, ItemSale, Item

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = '__all__'


class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'
        

class ArrivalForm(forms.ModelForm):
    class Meta:
        model = Arrival
        fields = '__all__'
        

class DepartureForm(forms.ModelForm):
    class Meta:
        model = Departure
        fields = '__all__'
        

class ItemSaleForm(forms.ModelForm):
    class Meta:
        model = ItemSale
        fields = '__all__'
        

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'




# class CustomLoginForm(forms.Form):
#     username = forms.CharField(label='Username')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)