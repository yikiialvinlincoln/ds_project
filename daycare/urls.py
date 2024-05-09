from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='indexpage'),

    #Sitter paths
    path('sitters/', views.sitter_list, name='sitter_list'),
    path('new_sitter/', views.new_sitter, name='new_sitter'),
    path('sitters/<int:sitter_id>/', views.sitter_details, name='sitter_details'),
    path('sitter_edit/<int:sitter_id>/', views.sitter_edit, name='sitter_edit'),
    path('sitter_delete/<int:sitter_id>/', views.sitter_delete, name='sitter_delete'),

    #Baby paths
    path('babies/', views.baby_list, name='baby_list'),
    path('new_baby/', views.new_baby, name='new_baby'),
    path('baby_detail/<int:baby_id>/', views.baby_detail, name='baby_detail'),
    path('baby_edit/<int:baby_id>/', views.baby_edit, name='baby_edit'),
    path('baby_delete/<int:baby_id>/', views.baby_delete, name='baby_delete'),

    #Arrival paths
    path('arrivals/', views.arrival_list, name='arrival_list'),
    path('new_arrival/', views.new_arrival, name='new_arrival'),
    path('arrival_edit/<int:arrival_id>/', views.arrival_edit, name='arrival_edit'),
    path('arrival_delete/<int:arrival_id>/', views.arrival_delete, name='arrival_delete'),

    #Departure paths
    path('departures/', views.departure_list, name='departure_list'),
    path('new_departure/', views.new_departure, name='new_departure'),
    path('departure_edit/<int:departure_id>/', views.departure_edit, name='departure_edit'),
    path('departure_delete/<int:departure_id>/', views.departure_delete, name='departure_delete'),

    #ItemSale paths
    path('itemsale_list/', views.itemsale_list, name='itemsale_list'),
    path('new_itemsale/', views.new_itemsale, name='new_itemsale'),
    path('itemsale_edit/<int:itemsale_id>/', views.itemsale_edit, name='itemsale_edit'),
    path('itemsale_delete/<int:itemsale_id>/', views.itemsale_delete, name='itemsale_delete'),

    #Item paths
    path('item_list/', views.item_list, name='item_list'),
    path('new_item/', views.new_item, name='new_item'),
    path('item_edit/<int:item_id>/', views.item_edit, name='item_edit'),
    path('item_delete/<int:item_id>/', views.item_delete, name='item_delete'),
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #path('about/', views.about,name='aboutpage'),
    # path('contact/', views.contact,name='contactpage'),
    #path('login/', views.login,name='loginpage'),
    # path('register/', views.register,name='registerpage'),
    # path('logout/', views.logout,name='logoutpage'),
    # Sitter URLs
    #path('sitters/', views.sitter_list, name='sitter_list'),
    #path('sitters/<int:sitter_id>/', views.sitter_detail, name='sitter_detail'),
    
    # Baby URLs
    #path('babies/', views.baby_list, name='baby_list'),
    #path('babies/<int:baby_id>/', views.baby_detail, name='baby_detail'),
    
    # Attendance URL
    #path('attendance/', views.attendance_list, name='attendance_list'),
    
    # Payment URL
    #path('payments/', views.payment_list, name='payment_list'),
    
    # Procurement URL
    #path('procurement/', views.procurement_list, name='procurement_list'),
]
