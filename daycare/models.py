from django.db import models
from django.utils import timezone

# Create your models here.
class Staytype(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name


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
    sitter_number = models.CharField(max_length=8,  unique=True,blank=False, null=True)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.s_name

class Sitterattendance(models.Model):
    sitter_number = models.CharField(max_length=200,unique=True)
    s_name = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=15, default='on-duty')

    def __str__(self):
        return str(self.s_name)
            

class Baby(models.Model):
    GENDER = {
        ('M', 'Male'),
        ('F', 'Female')
    }
    b_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER)
    age = models.CharField(max_length=10)
    location = models.CharField(max_length=15, default='')
    parents_names = models.CharField(max_length=15)
    fee_in_SHS = models.IntegerField()
    assigned_to = models.ForeignKey(Sitterattendance, on_delete=models.CASCADE)
    period_of_stay = models.ForeignKey(Staytype, on_delete=models.CASCADE)
    brought_by = models.CharField(max_length=200)
    baby_number = models.CharField(max_length=200, unique=True,blank=False, null=True)
    time_in = models.DateTimeField()

    def __str__(self):
        return self.b_name


class Departure(models.Model):
    b_name = models.ForeignKey(Baby,on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    picked_by = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    timed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.b_name


class Doll_type(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name

class Doll(models.Model):
    t_name = models.ForeignKey(Doll_type,on_delete=models.CASCADE,null=True, blank=True)
    doll_name = models.CharField(max_length=200,null=True, blank=True)
    quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=200,null=True, blank=True)
    size = models.CharField(max_length=200,null=True, blank=True)
    quantity_issued = models.IntegerField(default=0,null=True, blank=True)
    quantity_received = models.IntegerField(default=0,null=True, blank=True)          
    unit_price = models.IntegerField(default=0,null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.doll_name      

class Sales(models.Model):
    doll = models.ForeignKey(Doll, on_delete=models.CASCADE,null=False, blank=False)
    b_name = models.ForeignKey(Baby, on_delete=models.CASCADE)
    paid_by = models.CharField(max_length=200,null= True)
    quantity_sold = models.IntegerField(default=0)
    received_amount = models.IntegerField(default=0)
    date_sold = models.DateField(default=timezone.now)
    unit_price = models.IntegerField(default=0)
    
    def comp_total(self):
        total = self.quantity_sold * self.unit_price
        return int(total)

    def comp_balance(self):
        balance = self.comp_total - self.received_amount()
        return int(balance)    

class Babypayment(models.Model):
    b_name = models.CharField(max_length=200)
    paid_on = models.DateField()
    full_day = models.BooleanField(default=False,blank=True)       
    half_day = models.BooleanField(default=False,blank=True)       
    monthly_h = models.BooleanField(default=False,blank=True)       
    monthly_f = models.BooleanField(default=False,blank=True)    
    amount_due = models.DecimalField(max_digits=15,decimal_places=2,blank=True)
    paid_amount = models.DecimalField(max_digits=15,decimal_places=2) 
    balance_left = models.DecimalField(max_digits=15,decimal_places=2,default=0, blank=True)

    def __str__(self):
        return self.b_name

class Sitterpayment(models.Model):
    s_name = models.ForeignKey(Sitterattendance, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    baby_count = models.IntegerField(default=0)
    amount = models.IntegerField(default=3000)

    def __str__(self):
        return f"Sitter payment - {self.s_name}"

    def total_amount(self):
        total = self.amount * self.baby_count
        return int(total)             

class Item(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True) 
    def __str__(self):
        return self.name    

class Stock(models.Model):
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE,null=True,blank=True) 
    purchased_on = models.DateField(default=timezone.now)
    quantity_bought = models.IntegerField(default='')    
    amount_UGX = models.IntegerField(default='')
    quantity_issued_out = models.IntegerField(default='')   
    quantity_in_stock = models.IntegerField(default='')   
    #available_stock = models.IntegerField(default=0)   

    def __str__(self):
        return str(self.item_name)

    #def available_stock(self):
        quantitytotal = self.available_stock + self.quantity_bought
        return int(quantitytotal)

class Issuing(models.Model):
    quantity_issued_out = models.IntegerField(default=0)            
        


