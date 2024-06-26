from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission

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
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    b_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField()
    location = models.CharField(max_length=50, default='')
    parents_names = models.CharField(max_length=50)
    fee_in_SHS = models.IntegerField()
    assigned_to = models.ForeignKey(Sitterattendance, on_delete=models.CASCADE)
    period_of_stay = models.ForeignKey(Staytype, on_delete=models.CASCADE)
    brought_by = models.CharField(max_length=200)
    baby_number = models.CharField(max_length=200, unique=True, blank=False, null=True)
    time_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.b_name

class Departure(models.Model):
    b_name = models.ForeignKey(Baby, on_delete=models.CASCADE)
    departure_time = models.DateTimeField(auto_now_add=True)
    picked_by = models.CharField(max_length=100)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.b_name} - {self.time_of_departure}"


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
    doll = models.ForeignKey('Doll', on_delete=models.CASCADE, null=False, blank=False)
    doll_type = models.ForeignKey('Doll_type', on_delete=models.CASCADE, null=True, blank=True)
    b_name = models.ForeignKey('Baby', on_delete=models.CASCADE)
    paid_by = models.CharField(max_length=200, null=True)
    quantity_sold = models.IntegerField(default=0)
    received_amount = models.IntegerField(default=0)
    date_sold = models.DateField(default=timezone.now)
    unit_price = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Sale of {self.doll} ({self.doll_type}) to {self.b_name} on {self.date_sold}"
    
    @property
    def comp_total(self):
        return self.quantity_sold * self.unit_price

    @property
    def comp_balance(self):
        return self.comp_total - self.received_amount

class Babypayment(models.Model):
    b_name = models.CharField(max_length=200)
    paid_on = models.DateField(default=timezone.now)
    full_day = models.BooleanField(default=False, blank=True)       
    half_day = models.BooleanField(default=False, blank=True)       
    amount_due = models.DecimalField(max_digits=15, decimal_places=0, blank=True)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=0) 
    balance_left = models.DecimalField(max_digits=15, decimal_places=0, default=0, blank=True)

    def __str__(self):
        return self.b_name

    def save(self, *args, **kwargs):
        # Calculate the balance left before saving the instance
        if self.amount_due and self.paid_amount:
            self.balance_left = self.amount_due - self.paid_amount
        super().save(*args, **kwargs)

class Sitterpayment(models.Model):
    s_name = models.ForeignKey('Sitterattendance', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    baby_count = models.IntegerField(default=0)
    amount = models.IntegerField(default=3000)
    total_amount = models.IntegerField(default=0)  # This will store the computed total amount

    def __str__(self):
        return f"Sitter payment - {self.s_name}"

    def save(self, *args, **kwargs):
        self.total_amount = self.amount * self.baby_count
        super().save(*args, **kwargs)       

class Item(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return self.name    

class Stock(models.Model):
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    purchased_on = models.DateField(default=timezone.now)
    quantity_bought = models.IntegerField(default=0)
    quantity_issued_out = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.item_name.name) if self.item_name else "No Item Name"

    @property
    def available_stock(self):
        return self.quantity_bought - self.quantity_issued_out

class Issuing(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    issued_to = models.CharField(max_length=100)
    quantity = models.IntegerField()
    issue_date = models.DateField()

    def __str__(self):
        return f'{self.stock} issued to {self.issued_to}'
    


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # Specifies unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_groups',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_permissions', 
        related_query_name='user'
    )

    def _str_(self):
        return self.username
        


