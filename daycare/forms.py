from django import forms
from .models import *
from .models import Staytype, Sitter, Sitterattendance, Baby, Departure, Doll_type, Doll, Sales, Babypayment, Sitterpayment, Item, Stock, Issuing

class StaytypeForm(forms.ModelForm):
    class Meta:
        model = Staytype
        fields = ['name']

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = ['s_name', 'location', 'date_of_birth', 'gender', 'next_of_kin', 'nin', 'recommender_name', 'religion', 'education_level', 'sitter_number', 'contact']

class SitterattendanceForm(forms.ModelForm):
    class Meta:
        model = Sitterattendance
        fields = ['sitter_number', 's_name', 'date', 'status']

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['b_name', 'gender', 'age', 'location', 'parents_names', 'fee_in_SHS', 'assigned_to', 'period_of_stay', 'brought_by', 'baby_number', 'time_in']

class DepartureForm(forms.ModelForm):
    class Meta:
        model = Departure
        fields = ['b_name', 'departure_time', 'picked_by', 'comment']

class Doll_typeForm(forms.ModelForm):
    class Meta:
        model = Doll_type
        fields = ['name']

class DollForm(forms.ModelForm):
    class Meta:
        model = Doll
        fields = ['t_name', 'doll_name', 'quantity', 'color', 'size', 'quantity_issued', 'quantity_received', 'unit_price', 'date']

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['doll', 'b_name', 'paid_by', 'quantity_sold', 'received_amount', 'date_sold', 'unit_price']

class BabypaymentForm(forms.ModelForm):
    class Meta:
        model = Babypayment
        fields = ['b_name', 'paid_on', 'full_day', 'half_day', 'monthly_h', 'monthly_f', 'amount_due', 'paid_amount', 'balance_left']

class SitterpaymentForm(forms.ModelForm):
    class Meta:
        model = Sitterpayment
        fields = ['s_name', 'date', 'baby_count', 'amount']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item_name', 'purchased_on', 'quantity_bought', 'amount_UGX', 'quantity_issued_out', 'quantity_in_stock']

class IssuingForm(forms.ModelForm):
    class Meta:
        model = Issuing
        fields = ['quantity_issued_out']
