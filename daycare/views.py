from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StaytypeForm, SitterForm, BabyForm, DepartureForm, Doll_typeForm, DollForm, SalesForm, BabypaymentForm, SitterpaymentForm, ItemForm, StockForm, IssuingForm, SitterattendanceForm
# from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'daycare/index.html')

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
       

def list_sitters(request):
    sitters = Sitter.objects.all()
    return render(request, 'daycare/sitter_list.html', {'sitters': sitters})

def add_sitter(request):
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sitters')
    else:
        form = SitterForm()
    return render(request, 'daycare/sitter_form.html', {'form': form})

def view_sitter(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    return render(request, 'daycare/sitter_detail.html', {'sitter': sitter})

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

def delete_sitter(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            sitter.delete()
            return redirect('list_sitters')
        elif 'cancel' in request.POST:
            return redirect('list_sitters')
    return render(request, 'daycare/delete_sitter.html', {'sitter': sitter})


def list_sitter_attendance(request):
    sitter_attendance = Sitterattendance.objects.all()
    return render(request, 'daycare/sitterattendance_list.html', {'sitter_attendance': sitter_attendance})

def add_sitter_attendance(request):
    if request.method == 'POST':
        form = SitterattendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sitter_attendance')
    else:
        form = SitterattendanceForm()
    return render(request, 'daycare/sitterattendance_form.html', {'form': form})

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

def delete_sitter_attendance(request, attendance_id):
    attendance = get_object_or_404(Sitterattendance, pk=attendance_id)
    if request.method == 'POST':
        attendance.delete()
        return redirect('list_sitter_attendance')
    return render(request, 'daycare/sitterattendance_confirm_delete.html', {'attendance': attendance})


def list_babies(request):
    babies = Baby.objects.all()
    return render(request, 'daycare/baby_list.html', {'babies': babies})

def add_baby(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_babies')
    else:
        form = BabyForm()
    return render(request, 'daycare/baby_form.html', {'form': form})

def view_baby(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    return render(request, 'daycare/baby_detail.html', {'baby': baby})

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

def delete_baby(request, baby_id):
    baby = Baby.objects.get(pk=baby_id)
    if request.method == 'POST':
        baby.delete()
        return redirect('list_babies')
    return render(request, 'daycare/baby_confirm_delete.html', {'baby': baby})


def list_departures(request):
    departures = Departure.objects.all()
    return render(request, 'daycare/departure_list.html', {'departures': departures})

def add_departure(request):
    if request.method == 'POST':
        form = DepartureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_departures')
    else:
        form = DepartureForm()
    return render(request, 'daycare/departure_form.html', {'form': form})

def view_departure(request, departure_id):
    departure = get_object_or_404(Departure, pk=departure_id)
    return render(request, 'daycare/departure_detail.html', {'departure': departure})

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

def delete_departure(request, departure_id):
    departure = get_object_or_404(Departure, pk=departure_id)
    if request.method == 'POST':
        departure.delete()
        return redirect('list_departures')
    return render(request, 'daycare/departure_confirm_delete.html', {'departure': departure})

def list_doll_types(request):
    doll_types = Doll_type.objects.all()
    return render(request, 'daycare/doll_type_list.html', {'doll_types': doll_types})

def add_doll_type(request):
    if request.method == 'POST':
        form = Doll_typeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_doll_types')
    else:
        form = Doll_typeForm()
    return render(request, 'daycare/doll_type_form.html', {'form': form})

def view_doll_type(request, doll_type_id):
    doll_type = get_object_or_404(Doll_type, pk=doll_type_id)
    return render(request, 'daycare/doll_type_detail.html', {'doll_type': doll_type})

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

def delete_doll_type(request, doll_type_id):
    doll_type = get_object_or_404(Doll_type, pk=doll_type_id)
    if request.method == 'POST':
        doll_type.delete()
        return redirect('list_doll_types')
    return render(request, 'daycare/doll_type_confirm_delete.html', {'doll_type': doll_type})


def list_dolls(request):
    dolls = Doll.objects.all()
    return render(request, 'daycare/doll_list.html', {'dolls': dolls})

def add_doll(request):
    if request.method == 'POST':
        form = DollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_dolls')
    else:
        form = DollForm()
    return render(request, 'daycare/doll_form.html', {'form': form})

def view_doll(request, doll_id):
    doll = get_object_or_404(Doll, pk=doll_id)
    return render(request, 'daycare/doll_detail.html', {'doll': doll})

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

def delete_doll(request, doll_id):
    doll = get_object_or_404(Doll, pk=doll_id)
    if request.method == 'POST':
        doll.delete()
        return redirect('list_dolls')
    return render(request, 'daycare/doll_confirm_delete.html', {'doll': doll})


def list_sales(request):
    sales = Sales.objects.all()
    return render(request, 'daycare/sales_list.html', {'sales': sales})

def add_sales(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sales')
    else:
        form = SalesForm()
    return render(request, 'daycare/sales_form.html', {'form': form})

def view_sales(request, sales_id):
    sales = get_object_or_404(Sales, pk=sales_id)
    return render(request, 'daycare/sales_detail.html', {'sales': sales})

def edit_sales(request, sales_id):
    sales = get_object_or_404(Sales, pk=sales_id)
    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sales)
        if form.is_valid():
            form.save()
            return redirect('list_sales')
    else:
        form = SalesForm(instance=sales)
    return render(request, 'daycare/sales_form.html', {'form': form})

def delete_sales(request, sale_id):
    sale = get_object_or_404(Sales, id=sale_id)
    if request.method == 'POST':
        sale.delete()
        return redirect('list_sales')
    return render(request, 'daycare/delete_sales.html', {'sale': sale})

def babypayments_list(request):
    babypayments = Babypayment.objects.all()
    return render(request, 'daycare/babypayments_list.html', {'babypayments': babypayments})

def add_babypayment(request):
    if request.method == 'POST':
        form = BabypaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('babypayments_list')  # Ensure this URL pattern is defined
    else:
        form = BabypaymentForm()
    return render(request, 'daycare/add_babypayment.html', {'form': form})

def view_babypayment(request, babypayment_id):
    babypayment = get_object_or_404(Babypayment, pk=babypayment_id)
    return render(request, 'daycare/babypayment_detail.html', {'babypayment': babypayment})

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

def delete_babypayment(request, babypayment_id):
    babypayment = get_object_or_404(Babypayment, pk=babypayment_id)
    if request.method == 'POST':
        babypayment.delete()
        return redirect('list_babypayments')
    return render(request, 'daycare/babypayment_confirm_delete.html', {'babypayment': babypayment})    


def sitterpayments_list(request):
    sitterpayments = Sitterpayment.objects.all()
    return render(request, 'daycare/sitterpayments_list.html', {'sitterpayments': sitterpayments})

def add_sitter_payment(request):
    if request.method == 'POST':
        form = SitterpaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sitterpayments_list')
    else:
        form = SitterpaymentForm()
    return render(request, 'daycare/add_sitter_payment.html', {'form': form})

def view_sitterpayment(request, sitterpayment_id):
    sitterpayment = get_object_or_404(Sitterpayment, pk=sitterpayment_id)
    return render(request, 'daycare/sitterpayment_detail.html', {'sitterpayment': sitterpayment})

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

def delete_sitterpayment(request, sitterpayment_id):
    sitterpayment = get_object_or_404(Sitterpayment, pk=sitterpayment_id)
    if request.method == 'POST':
        sitterpayment.delete()
        return redirect('list_sitterpayments')
    return render(request, 'daycare/sitterpayment_confirm_delete.html', {'sitterpayment': sitterpayment})

def list_items(request):
    items = Item.objects.all()
    return render(request, 'daycare/item_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ItemForm()
    return render(request, 'daycare/item_form.html', {'form': form})

def view_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'daycare/item_detail.html', {'item': item})

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

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('list_items')
    return render(request, 'daycare/item_confirm_delete.html', {'item': item})    

def list_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'daycare/list_stock.html', {'stocks': stocks})

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_stock')
    else:
        form = StockForm()
    return render(request, 'daycare/stock_form.html', {'form': form})

def view_stock(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    return render(request, 'daycare/view_stock.html', {'stock': stock})


def edit_stock(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('list_stock')
    else:
        form = StockForm(instance=stock)
    return render(request, 'daycare/stock_form.html', {'form': form})

def delete_stock(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        stock.delete()
        return redirect('list_stock')
    return render(request, 'daycare/stock_confirm_delete.html', {'stock': stock})    

def list_issuing(request):
    issuings = Issuing.objects.all()
    return render(request, 'daycare/issuing_list.html', {'issuings': issuings})

def add_issuing(request):
    if request.method == 'POST':
        form = IssuingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_issuing')
    else:
        form = IssuingForm()
    return render(request, 'daycare/issuing_form.html', {'form': form})

def view_issuing(request, issuing_id):
    issuing = get_object_or_404(Issuing, pk=issuing_id)
    return render(request, 'daycare/issuing_detail.html', {'issuing': issuing})

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

def delete_issuing(request, issuing_id):
    issuing = get_object_or_404(Issuing, pk=issuing_id)
    if request.method == 'POST':
        issuing.delete()
        return redirect('list_issuing')
    return render(request, 'daycare/issuing_confirm_delete.html', {'issuing': issuing})
 


 


















