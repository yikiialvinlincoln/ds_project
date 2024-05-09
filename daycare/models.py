from django.db import models
#from django.utils import timezone

# Create your models here.
class Sitter(models.Model):
    s_name = models.CharField(max_length=20)
    location = models.CharField(max_length=20, default='Kabalagala')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    next_of_kin = models.CharField(max_length=20)
    nin = models.CharField(max_length=20)
    recommender_name = models.CharField(max_length=20)
    religion = models.CharField(max_length=25, blank=True)
    education_level = models.CharField(max_length=255)
    sitter_number = models.CharField(max_length=8)
    contacts = models.CharField(max_length=15)

    def __str__(self):
        return self.s_name

class Baby(models.Model):
    sitter = models.ForeignKey(Sitter,on_delete=models.CASCADE, null=True)
    b_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    age = models.IntegerField()
    location = models.CharField(max_length=15, default='')
    parents_names = models.CharField(max_length=15)
    fee = models.IntegerField()
    period_of_stay = models.CharField(max_length=20)
    baby_number = models.CharField(max_length=8)

    def __str__(self):
        return self.b_name


class Arrival(models.Model):
    baby = models.ForeignKey(Baby,on_delete=models.CASCADE, null=True)
    arrival_time = models.TimeField()
    brought_by = models.CharField(max_length=15)
    
    def __str__(self):
        return self.baby.b_name


class Departure(models.Model):
    baby = models.ForeignKey(Baby,on_delete=models.CASCADE, null=True)
    departure_time = models.TimeField()
    parents_names = models.CharField(max_length=15)
    
    def __str__(self):
        return self.baby.b_name


class ItemSale(models.Model):
    item_name = models.CharField(max_length=15)
    quantity = models.IntegerField()
    total_cost = models.IntegerField(null=False, blank=True)
    payee = models.CharField(max_length=20) 
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.payee 

class Item(models.Model):
    item_name = models.CharField(max_length=15)
    quantity = models.IntegerField()
    unit_price = models.IntegerField(null=False, blank=True) 

    def __str__(self):
        return self.item_name    
        



