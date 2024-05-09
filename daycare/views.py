from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SitterForm, BabyForm, ArrivalForm, DepartureForm, ItemSaleForm, ItemForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'daycare/index.html')


def sitter_list(request):
    sitters = Sitter.objects.all()
    return render(request, 'daycare/sitter_list.html', {'sitters': sitters})

def sitter_details(request, sitter_id):
    sitter = Sitter.objects.get(pk=sitter_id)
    return render(request, 'daycare/sitter_details.html', {'sitter': sitter})   

def new_sitter(request):
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sitter added successfully!')
            return redirect('sitter_list')
    else:
        form = SitterForm()
    
    return render(request, 'daycare/new_sitter.html', {'form': form})     

def sitter_edit(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    if request.method == 'POST':
        form = SitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            return redirect('sitter_details', sitter_id=sitter_id)
    else:
        form = SitterForm(instance=sitter)
    return render(request, 'daycare/sitter_edit.html', {'form': form})

def sitter_delete(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    if request.method == 'POST':
        sitter.delete()
        return redirect('sitter_list')
    return render(request, 'daycare/sitter_delete.html', {'sitter': sitter})    


def baby_list(request):
    babies = Baby.objects.all()
    return render(request, 'daycare/baby_list.html', {'babies': babies}) 

def new_baby(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Baby added successfully!')
            return redirect('baby_list')  
    else:
        form = BabyForm()
    
    return render(request, 'daycare/new_baby.html', {'form': form})


def baby_detail(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    return render(request, 'daycare/baby_detail.html', {'baby': baby})    


def baby_edit(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    if request.method == 'POST':
        form = BabyForm(request.POST, instance=baby)
        if form.is_valid():
            form.save()
            return redirect('baby_detail', baby_id=baby_id)
    else:
        form = BabyForm(instance=baby)
    
    return render(request, 'daycare/baby_edit.html', {'form': form, 'baby': baby})


def baby_delete(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    if request.method == 'POST':
        baby.delete()
        return redirect('baby_list')  
    
    return render(request, 'daycare/baby_delete.html', {'baby': baby})


def arrival_list(request):
    arrivals = Arrival.objects.all()
    return render(request, 'daycare/arrival_list.html', {'arrivals': arrivals})


def new_arrival(request):
    if request.method == 'POST':
        form = ArrivalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('arrival_list')
    else:
        form = ArrivalForm()
    
    return render(request, 'daycare/new_arrival.html', {'form': form})    


def arrival_edit(request, arrival_id):
    arrival = get_object_or_404(Arrival, pk=arrival_id)
    if request.method == 'POST':
        form = ArrivalForm(request.POST, instance=arrival)
        if form.is_valid():
            form.save()
            return redirect('arrival_list')
    else:
        form = ArrivalForm(instance=arrival)
    
    return render(request, 'daycare/arrival_edit.html', {'form': form, 'arrival': arrival})   


def arrival_delete(request, arrival_id):
    arrival = get_object_or_404(Arrival, pk=arrival_id)
    if request.method == 'POST':
        arrival.delete()
        return redirect('arrival_list')
    
    return render(request, 'daycare/arrival_delete.html', {'arrival': arrival})     


def departure_list(request):
    departures = Departure.objects.all()
    return render(request, 'daycare/departure_list.html', {'departures': departures})  


def new_departure(request):
    if request.method == 'POST':
        form = DepartureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departure_list')
    else:
        form = DepartureForm()
    
    return render(request, 'daycare/new_departure.html', {'form': form})


def departure_edit(request, departure_id):
    departure = get_object_or_404(Departure, pk=departure_id)
    if request.method == 'POST':
        form = DepartureForm(request.POST, instance=departure)
        if form.is_valid():
            form.save()
            return redirect('departure_list')
    else:
        form = DepartureForm(instance=departure)
    
    return render(request, 'daycare/departure_edit.html', {'form': form, 'departure': departure})

def departure_delete(request, departure_id):
    departure = get_object_or_404(Departure, pk=departure_id)
    if request.method == 'POST':
        departure.delete()
        return redirect('departure_list')
    
    return render(request, 'daycare/departure_delete.html', {'departure': departure})    


def itemsale_list(request):
    itemsales = ItemSale.objects.all()
    return render(request, 'daycare/itemsale_list.html', {'itemsales': itemsales})   

def new_itemsale(request):
    if request.method == 'POST':
        form = ItemSaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itemsale_list')
    else:
        form = ItemSaleForm()
    
    return render(request, 'daycare/new_itemsale.html', {'form': form})   


def itemsale_edit(request, itemsale_id):
    itemsale = get_object_or_404(ItemSale, pk=itemsale_id)
    if request.method == 'POST':
        form = ItemSaleForm(request.POST, instance=itemsale)
        if form.is_valid():
            form.save()
            return redirect('itemsale_list')
    else:
        form = ItemSaleForm(instance=itemsale)
    
    return render(request, 'daycare/itemsale_edit.html', {'form': form, 'itemsale': itemsale})

def itemsale_delete(request, itemsale_id):
    itemsale = get_object_or_404(ItemSale, pk=itemsale_id)
    if request.method == 'POST':
        itemsale.delete()
        return redirect('itemsale_list')
    
    return render(request, 'daycare/itemsale_delete.html', {'itemsale': itemsale})      


def item_list(request):
    items = Item.objects.all()
    return render(request, 'daycare/item_list.html', {'items': items})

def new_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    
    return render(request, 'daycare/new_item.html', {'form': form})


def item_edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'daycare/item_edit.html', {'form': form, 'item': item})

def item_delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    
    return render(request, 'daycare/item_delete.html', {'item': item})    


# def custom_login(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to the home page after login
#             else:
#                 form.add_error(None, 'Invalid username or password')
#     else:
#         form = CustomLoginForm()
    
#     return render(request, 'daycare/login.html', {'form': form})    


















