from django import forms
from .models import Staytype, Sitter, Sitterattendance, Baby, Departure, Doll_type, Doll, Sales, Babypayment, Sitterpayment, Item, Stock, Issuing

class StaytypeForm(forms.ModelForm):
    class Meta:
        model = Staytype
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required.')
        return name

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = ['s_name', 'location', 'date_of_birth', 'gender', 'next_of_kin', 'nin', 'recommender_name', 'religion', 'education_level', 'sitter_number', 'contact']

    def clean_s_name(self):
        s_name = self.cleaned_data.get('s_name')
        if not s_name:
            raise forms.ValidationError('This field is required.')
        return s_name

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if not location:
            raise forms.ValidationError('This field is required.')
        return location

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if not date_of_birth:
            raise forms.ValidationError('This field is required.')
        return date_of_birth

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError('This field is required.')
        return gender

    def clean_next_of_kin(self):
        next_of_kin = self.cleaned_data.get('next_of_kin')
        if not next_of_kin:
            raise forms.ValidationError('This field is required.')
        return next_of_kin

    def clean_nin(self):
        nin = self.cleaned_data.get('nin')
        if not nin:
            raise forms.ValidationError('This field is required.')
        return nin

    def clean_recommender_name(self):
        recommender_name = self.cleaned_data.get('recommender_name')
        if not recommender_name:
            raise forms.ValidationError('This field is required.')
        return recommender_name

    def clean_religion(self):
        religion = self.cleaned_data.get('religion')
        if not religion:
            raise forms.ValidationError('This field is required.')
        return religion

    def clean_education_level(self):
        education_level = self.cleaned_data.get('education_level')
        if not education_level:
            raise forms.ValidationError('This field is required.')
        return education_level

    def clean_sitter_number(self):
        sitter_number = self.cleaned_data.get('sitter_number')
        if not sitter_number:
            raise forms.ValidationError('This field is required.')
        return sitter_number

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not contact:
            raise forms.ValidationError('This field is required.')
        return contact

class SitterattendanceForm(forms.ModelForm):
    class Meta:
        model = Sitterattendance
        fields = ['sitter_number', 's_name', 'date', 'status']

    def clean_sitter_number(self):
        sitter_number = self.cleaned_data.get('sitter_number')
        if not sitter_number:
            raise forms.ValidationError('This field is required.')
        return sitter_number

    def clean_s_name(self):
        s_name = self.cleaned_data.get('s_name')
        if not s_name:
            raise forms.ValidationError('This field is required.')
        return s_name

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise forms.ValidationError('This field is required.')
        return date

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if not status:
            raise forms.ValidationError('This field is required.')
        return status

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        exclude = ['time_in']

class DepartureForm(forms.ModelForm):
    class Meta:
        model = Departure
        fields = ['b_name', 'departure_time', 'picked_by', 'comment']

    def clean_b_name(self):
        b_name = self.cleaned_data.get('b_name')
        if not b_name:
            raise forms.ValidationError('This field is required.')
        return b_name

    def clean_departure_time(self):
        departure_time = self.cleaned_data.get('departure_time')
        if not departure_time:
            raise forms.ValidationError('This field is required.')
        return departure_time

    def clean_picked_by(self):
        picked_by = self.cleaned_data.get('picked_by')
        if not picked_by:
            raise forms.ValidationError('This field is required.')
        return picked_by

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if not comment:
            raise forms.ValidationError('This field is required.')
        return comment

class Doll_typeForm(forms.ModelForm):
    class Meta:
        model = Doll_type
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required.')
        return name

class DollForm(forms.ModelForm):
    class Meta:
        model = Doll
        fields = ['t_name', 'doll_name', 'quantity', 'color', 'size', 'quantity_issued', 'quantity_received', 'unit_price', 'date']

    def clean_t_name(self):
        t_name = self.cleaned_data.get('t_name')
        if not t_name:
            raise forms.ValidationError('This field is required.')
        return t_name

    def clean_doll_name(self):
        doll_name = self.cleaned_data.get('doll_name')
        if not doll_name:
            raise forms.ValidationError('This field is required.')
        return doll_name

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if not quantity:
            raise forms.ValidationError('This field is required.')
        return quantity

    def clean_color(self):
        color = self.cleaned_data.get('color')
        if not color:
            raise forms.ValidationError('This field is required.')
        return color

    def clean_size(self):
        size = self.cleaned_data.get('size')
        if not size:
            raise forms.ValidationError('This field is required.')
        return size

    def clean_quantity_issued(self):
        quantity_issued = self.cleaned_data.get('quantity_issued')
        if not quantity_issued:
            raise forms.ValidationError('This field is required.')
        return quantity_issued

    def clean_quantity_received(self):
        quantity_received = self.cleaned_data.get('quantity_received')
        if not quantity_received:
            raise forms.ValidationError('This field is required.')
        return quantity_received

    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if not unit_price:
            raise forms.ValidationError('This field is required.')
        return unit_price

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise forms.ValidationError('This field is required.')
        return date

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['doll', 'b_name', 'paid_by', 'quantity_sold', 'received_amount', 'date_sold', 'unit_price']

    def clean_doll(self):
        doll = self.cleaned_data.get('doll')
        if not doll:
            raise forms.ValidationError('This field is required.')
        return doll

    def clean_b_name(self):
        b_name = self.cleaned_data.get('b_name')
        if not b_name:
            raise forms.ValidationError('This field is required.')
        return b_name

    def clean_paid_by(self):
        paid_by = self.cleaned_data.get('paid_by')
        if not paid_by:
            raise forms.ValidationError('This field is required.')
        return paid_by

    def clean_quantity_sold(self):
        quantity_sold = self.cleaned_data.get('quantity_sold')
        if not quantity_sold:
            raise forms.ValidationError('This field is required.')
        return quantity_sold

    def clean_received_amount(self):
        received_amount = self.cleaned_data.get('received_amount')
        if not received_amount:
            raise forms.ValidationError('This field is required.')
        return received_amount

    def clean_date_sold(self):
        date_sold = self.cleaned_data.get('date_sold')
        if not date_sold:
            raise forms.ValidationError('This field is required.')
        return date_sold

    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if not unit_price:
            raise forms.ValidationError('This field is required.')
        return unit_price

class BabypaymentForm(forms.ModelForm):
    class Meta:
        model = Babypayment
        fields = ['b_name', 'paid_on', 'full_day', 'half_day', 'amount_due', 'paid_amount', 'balance_left']
        widgets = {
            'b_name': forms.TextInput(attrs={'class': 'form-control'}),
            'paid_on': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'full_day': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'half_day': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'amount_due': forms.NumberInput(attrs={'class': 'form-control'}),
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'balance_left': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SitterpaymentForm(forms.ModelForm):
    class Meta:
        model = Sitterpayment
        fields = ['s_name', 'date', 'baby_count', 'amount']
        widgets = {
            's_name': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'baby_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required.')
        return name

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item_name', 'purchased_on', 'quantity_bought', 'amount_UGX', 'quantity_issued_out', 'quantity_in_stock']

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required.')
        return item_name

    def clean_purchased_on(self):
        purchased_on = self.cleaned_data.get('purchased_on')
        if not purchased_on:
            raise forms.ValidationError('This field is required.')
        return purchased_on

    def clean_quantity_bought(self):
        quantity_bought = self.cleaned_data.get('quantity_bought')
        if not quantity_bought:
            raise forms.ValidationError('This field is required.')
        return quantity_bought

    def clean_amount_UGX(self):
        amount_UGX = self.cleaned_data.get('amount_UGX')
        if not amount_UGX:
            raise forms.ValidationError('This field is required.')
        return amount_UGX

    def clean_quantity_issued_out(self):
        quantity_issued_out = self.cleaned_data.get('quantity_issued_out')
        if not quantity_issued_out:
            raise forms.ValidationError('This field is required.')
        return quantity_issued_out

    def clean_quantity_in_stock(self):
        quantity_in_stock = self.cleaned_data.get('quantity_in_stock')
        if not quantity_in_stock:
            raise forms.ValidationError('This field is required.')
        return quantity_in_stock

class IssuingForm(forms.ModelForm):
    class Meta:
        model = Issuing
        fields = ['quantity_issued_out']

    def clean_quantity_issued_out(self):
        quantity_issued_out = self.cleaned_data.get('quantity_issued_out')
        if not quantity_issued_out:
            raise forms.ValidationError('This field is required.')
        return quantity_issued_out

