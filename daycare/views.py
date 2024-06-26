from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StaytypeForm, SitterForm, BabyForm, DepartureForm, Doll_typeForm, DollForm, SalesForm, BabypaymentForm, SitterpaymentForm, ItemForm, StockForm, IssuingForm, SitterattendanceForm
from django.db import transaction
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


# Create your views here.

def index(request):
    return render(request, 'daycare/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            # Redirects to a success page or returns a success message
            return redirect('home')  
        else:
            # Returns an invalid login message
            return render(request, 'daycare/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'daycare/login.html')
    

def custom_logout(request):
    if request.method == 'POST':
        confirm_choice = request.POST.get('confirm')
        if confirm_choice == 'yes':
            # Performs logout
            # Redirects you to the index page
            return redirect('/')
        elif confirm_choice == 'no':
            # Redirects you to the dashboard
            return redirect('home')
    else:
        # Handles the GET request
        return render(request, 'daycare/logout.html')    

@login_required
def home(request):
    #Data Analysis
    count_babies = Baby.objects.count()
    count_sitters = Sitter.objects.count()
    count_departure = Departure.objects.count()
    count_sitterattendance = Sitterattendance.objects.count()
    context = {
        "count_babies": count_babies,
        "count_sitters": count_sitters,
        "count_departure": count_departure,
        "count_sitterattendance": count_sitterattendance,
    }
    return render(request, 'daycare/home.html', context)
       
@login_required
def list_sitters(request):
    sitters = Sitter.objects.all()
    return render(request, 'daycare/sitter_list.html', {'sitters': sitters})


@login_required
def add_sitter(request):
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sitters')
    else:
        form = SitterForm()
    return render(request, 'daycare/sitter_form.html', {'form': form})


@login_required
def view_sitter(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    return render(request, 'daycare/sitter_detail.html', {'sitter': sitter})


@login_required
def edit_sitter(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    if request.method == 'POST':
        form = SitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            return redirect('list_sitters')
    else:
        form = SitterForm(instance=sitter)
    return render(request, 'daycare/sitter_form.html', {'form': form})


@login_required
def delete_sitter(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            sitter.delete()
            return redirect('list_sitters')
        elif 'cancel' in request.POST:
            return redirect('list_sitters')
    return render(request, 'daycare/delete_sitter.html', {'sitter': sitter})


@login_required
def list_sitter_attendance(request):
    sitter_attendance = Sitterattendance.objects.all()
    return render(request, 'daycare/sitterattendance_list.html', {'sitter_attendance': sitter_attendance})


@login_required
def add_sitter_attendance(request):
    if request.method == 'POST':
        form = SitterattendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sitter_attendance')
    else:
        form = SitterattendanceForm()
    return render(request, 'daycare/sitterattendance_form.html', {'form': form})


@login_required
def edit_sitter_attendance(request, attendance_id):
    attendance = get_object_or_404(Sitterattendance, pk=attendance_id)
    if request.method == 'POST':
        form = SitterattendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('list_sitter_attendance')
    else:
        form = SitterattendanceForm(instance=attendance)
    return render(request, 'daycare/sitterattendance_form.html', {'form': form})


@login_required
def delete_sitter_attendance(request, attendance_id):
    attendance = get_object_or_404(Sitterattendance, pk=attendance_id)
    if request.method == 'POST':
        attendance.delete()
        return redirect('list_sitter_attendance')
    return render(request, 'daycare/sitterattendance_confirm_delete.html', {'attendance': attendance})


@login_required
def list_babies(request):
    babies = Baby.objects.all()
    return render(request, 'daycare/baby_list.html', {'babies': babies})


@login_required
def add_baby(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_babies')
    else:
        form = BabyForm()
    return render(request, 'daycare/baby_form.html', {'form': form})


@login_required
def view_baby(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    return render(request, 'daycare/baby_detail.html', {'baby': baby})


@login_required
def edit_baby(request, baby_id):
    baby = Baby.objects.get(pk=baby_id)
    if request.method == 'POST':
        form = BabyForm(request.POST, instance=baby)
        if form.is_valid():
            form.save()
            return redirect('list_babies')
    else:
        form = BabyForm(instance=baby)
    return render(request, 'daycare/baby_form.html', {'form': form})


@login_required
def delete_baby(request, baby_id):
    baby = Baby.objects.get(pk=baby_id)
    if request.method == 'POST':
        baby.delete()
        return redirect('list_babies')
    return render(request, 'daycare/baby_confirm_delete.html', {'baby': baby})


@login_required
def list_departures(request):
    departures = Departure.objects.all()
    return render(request, 'daycare/departure_list.html', {'departures': departures})

@login_required
def add_departure(request):
    if request.method == 'POST':
        form = DepartureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_departures')
    else:
        form = DepartureForm()
    return render(request, 'daycare/departure_form.html', {'form': form})


@login_required
def view_departure(request, departure_id):
    departure = get_object_or_404(Departure, pk=departure_id)
    return render(request, 'daycare/departure_detail.html', {'departure': departure})


@login_required
def edit_departure(request, departure_id):
    departure = get_object_or_404(Departure, pk=departure_id)
    if request.method == 'POST':
        form = DepartureForm(request.POST, instance=departure)
        if form.is_valid():
            form.save()
            return redirect('list_departures')
    else:
        form = DepartureForm(instance=departure)
    return render(request, 'daycare/departure_form.html', {'form': form})


@login_required
def delete_departure(request, departure_id):
    departure = get_object_or_404(Departure, pk=departure_id)
    if request.method == 'POST':
        departure.delete()
        return redirect('list_departures')
    return render(request, 'daycare/departure_confirm_delete.html', {'departure': departure})


@login_required
def list_doll_types(request):
    doll_types = Doll_type.objects.all()
    return render(request, 'daycare/doll_type_list.html', {'doll_types': doll_types})


@login_required
def add_doll_type(request):
    if request.method == 'POST':
        form = Doll_typeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_doll_types')
    else:
        form = Doll_typeForm()
    return render(request, 'daycare/doll_type_form.html', {'form': form})


@login_required
def view_doll_type(request, doll_type_id):
    doll_type = get_object_or_404(Doll_type, pk=doll_type_id)
    return render(request, 'daycare/doll_type_detail.html', {'doll_type': doll_type})


@login_required
def edit_doll_type(request, doll_type_id):
    doll_type = get_object_or_404(Doll_type, pk=doll_type_id)
    if request.method == 'POST':
        form = Doll_typeForm(request.POST, instance=doll_type)
        if form.is_valid():
            form.save()
            return redirect('list_doll_types')
    else:
        form = Doll_typeForm(instance=doll_type)
    return render(request, 'daycare/doll_type_form.html', {'form': form})


@login_required
def delete_doll_type(request, doll_type_id):
    doll_type = get_object_or_404(Doll_type, pk=doll_type_id)
    if request.method == 'POST':
        doll_type.delete()
        return redirect('list_doll_types')
    return render(request, 'daycare/doll_type_confirm_delete.html', {'doll_type': doll_type})


@login_required
def list_dolls(request):
    dolls = Doll.objects.all()
    return render(request, 'daycare/doll_list.html', {'dolls': dolls})


@login_required
def add_doll(request):
    if request.method == 'POST':
        form = DollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_dolls')
    else:
        form = DollForm()
    return render(request, 'daycare/doll_form.html', {'form': form})


@login_required
def view_doll(request, doll_id):
    doll = get_object_or_404(Doll, pk=doll_id)
    return render(request, 'daycare/doll_detail.html', {'doll': doll})


@login_required
def edit_doll(request, doll_id):
    doll = get_object_or_404(Doll, pk=doll_id)
    if request.method == 'POST':
        form = DollForm(request.POST, instance=doll)
        if form.is_valid():
            form.save()
            return redirect('list_dolls')
    else:
        form = DollForm(instance=doll)
    return render(request, 'daycare/doll_form.html', {'form': form})


@login_required
def delete_doll(request, doll_id):
    doll = get_object_or_404(Doll, pk=doll_id)
    if request.method == 'POST':
        doll.delete()
        return redirect('list_dolls')
    return render(request, 'daycare/doll_confirm_delete.html', {'doll': doll})


@login_required
def list_sales(request):
    sales = Sales.objects.all()
    return render(request, 'daycare/sales_list.html', {'sales': sales})


@login_required
def add_sales(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sales')
    else:
        form = SalesForm()
    return render(request, 'daycare/sales_form.html', {'form': form})


@login_required
def view_sales(request, pk):
    sale = get_object_or_404(Sales, pk=pk)
    return render(request, 'daycare/sales_detail.html', {'sale': sale})


@login_required
def edit_sales(request, pk):
    sale = get_object_or_404(Sales, pk=pk)
    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('view_sales', pk=sale.pk)
    else:
        form = SalesForm(instance=sale)
    return render(request, 'daycare/sales_form.html', {'form': form})

# @login_required
# def delete_sales(request, sale_id):
#     sale = get_object_or_404(Sales, id=sale_id)
#     if request.method == 'POST':
#         sale.delete()
#         return redirect('list_sales')
#     return render(request, 'daycare/delete_sales.html', {'sale': sale})


@login_required
def babypayments_list(request):
    babypayments = Babypayment.objects.all()
    return render(request, 'daycare/babypayments_list.html', {'babypayments': babypayments})


@login_required
def add_babypayment(request):
    if request.method == 'POST':
        form = BabypaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('babypayments_list')  # Ensure this URL pattern is defined
    else:
        form = BabypaymentForm()
    return render(request, 'daycare/add_babypayment.html', {'form': form})


@login_required
def view_babypayment(request, babypayment_id):
    babypayment = get_object_or_404(Babypayment, pk=babypayment_id)
    return render(request, 'daycare/babypayment_detail.html', {'babypayment': babypayment})


@login_required
def edit_babypayment(request, babypayment_id):
    babypayment = get_object_or_404(Babypayment, pk=babypayment_id)
    if request.method == 'POST':
        form = BabypaymentForm(request.POST, instance=babypayment)
        if form.is_valid():
            form.save()
            return redirect('list_babypayments')
    else:
        form = BabypaymentForm(instance=babypayment)
    return render(request, 'daycare/babypayment_form.html', {'form': form})


@login_required
def delete_babypayment(request, babypayment_id):
    babypayment = get_object_or_404(Babypayment, pk=babypayment_id)
    if request.method == 'POST':
        babypayment.delete()
        return redirect('list_babypayments')
    return render(request, 'daycare/babypayment_confirm_delete.html', {'babypayment': babypayment})    



@login_required
def sitterpayments_list(request):
    sitterpayments = Sitterpayment.objects.all()
    return render(request, 'daycare/sitterpayments_list.html', {'sitterpayments': sitterpayments})


@login_required
def add_sitter_payment(request):
    if request.method == 'POST':
        form = SitterpaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sitterpayments_list')
    else:
        form = SitterpaymentForm()
    return render(request, 'daycare/add_sitter_payment.html', {'form': form})


@login_required
def view_sitterpayment(request, sitterpayment_id):
    sitterpayment = get_object_or_404(Sitterpayment, pk=sitterpayment_id)
    return render(request, 'daycare/sitterpayment_detail.html', {'sitterpayment': sitterpayment})


@login_required
def edit_sitterpayment(request, sitterpayment_id):
    sitterpayment = get_object_or_404(Sitterpayment, pk=sitterpayment_id)
    if request.method == 'POST':
        form = SitterpaymentForm(request.POST, instance=sitterpayment)
        if form.is_valid():
            form.save()
            return redirect('list_sitterpayments')
    else:
        form = SitterpaymentForm(instance=sitterpayment)
    return render(request, 'daycare/sitterpayment_form.html', {'form': form})


@login_required
def delete_sitterpayment(request, sitterpayment_id):
    sitterpayment = get_object_or_404(Sitterpayment, pk=sitterpayment_id)
    if request.method == 'POST':
        sitterpayment.delete()
        return redirect('list_sitterpayments')
    return render(request, 'daycare/sitterpayment_confirm_delete.html', {'sitterpayment': sitterpayment})


@login_required
def list_items(request):
    items = Item.objects.all()
    return render(request, 'daycare/item_list.html', {'items': items})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ItemForm()
    return render(request, 'daycare/item_form.html', {'form': form})


@login_required
def view_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'daycare/item_detail.html', {'item': item})


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'daycare/item_form.html', {'form': form})


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('list_items')
    return render(request, 'daycare/item_confirm_delete.html', {'item': item})    


@login_required
def list_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'daycare/stock_list.html', {'stocks': stocks})


@login_required
def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_stock')
    else:
        form = StockForm()
    return render(request, 'daycare/stock_form.html', {'form': form})


@login_required
def view_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'daycare/stock_detail.html', {'stock': stock})


@login_required
def edit_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('view_stock', pk=stock.pk)
    else:
        form = StockForm(instance=stock)
    return render(request, 'daycare/stock_form.html', {'form': form})


@login_required
# def delete_stock(request, pk):
#     stock = get_object_or_404(Stock, pk=pk)
#     issuings = Issuing.objects.filter(stock=stock)
    
#     if request.method == 'POST':
#         with transaction.atomic():
#             # Delete all related issuings
#             issuings.delete()
#             # Delete the stock
#             stock.delete()
#             return redirect('list_stock')
    
#     return render(request, 'daycare/stock_confirm_delete.html', {'stock': stock})    


@login_required
def list_issuing(request):
    issuings = Issuing.objects.all()
    return render(request, 'daycare/issuing_list.html', {'issuings': issuings})


@login_required
def add_issuing(request):
    if request.method == 'POST':
        form = IssuingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_issuing')
    else:
        form = IssuingForm()
    return render(request, 'daycare/issuing_form.html', {'form': form})


@login_required
def view_issuing(request, issuing_id):
    issuing = get_object_or_404(Issuing, pk=issuing_id)
    return render(request, 'daycare/issuing_detail.html', {'issuing': issuing})


@login_required
def edit_issuing(request, issuing_id):
    issuing = get_object_or_404(Issuing, pk=issuing_id)
    if request.method == 'POST':
        form = IssuingForm(request.POST, instance=issuing)
        if form.is_valid():
            form.save()
            return redirect('list_issuing')
    else:
        form = IssuingForm(instance=issuing)
    return render(request, 'daycare/issuing_form.html', {'form': form})


@login_required
def delete_issuing(request, issuing_id):
    issuing = get_object_or_404(Issuing, pk=issuing_id)
    if request.method == 'POST':
        issuing.delete()
        return redirect('list_issuing')
    return render(request, 'daycare/issuing_confirm_delete.html', {'issuing': issuing})
 


 


















