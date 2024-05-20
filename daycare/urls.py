from django.urls import path
from . import views
from daycare.views import custom_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='indexpage'),
    # path('login/', auth_views.LoginView.as_view(template_name='daycare/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', custom_logout, name='logout'),

    #Sitter paths
    path('sitters/', views.list_sitters, name='list_sitters'),
    path('sitters/add/', views.add_sitter, name='add_sitter'),
    path('sitters/<int:sitter_id>/', views.view_sitter, name='view_sitter'),
    path('sitters/<int:sitter_id>/edit/', views.edit_sitter, name='edit_sitter'),
    path('delete_sitter/<int:sitter_id>/', views.delete_sitter, name='delete_sitter'),
    
    #Sitter attendance paths
    path('sitterattendance/', views.list_sitter_attendance, name='list_sitter_attendance'),
    path('sitterattendance/add/', views.add_sitter_attendance, name='add_sitter_attendance'),
    path('sitterattendance/<int:attendance_id>/edit/', views.edit_sitter_attendance, name='edit_sitter_attendance'),
    path('sitterattendance/<int:attendance_id>/delete/', views.delete_sitter_attendance, name='delete_sitter_attendance'),

    #Baby paths
    path('view_baby/<int:baby_id>/', views.view_baby, name='view_baby'),
    path('edit_baby/<int:baby_id>/', views.edit_baby, name='edit_baby'),
    path('delete_baby/<int:baby_id>/', views.delete_baby, name='delete_baby'),
    path('add_baby/', views.add_baby, name='add_baby'),
    path('list_babies/', views.list_babies, name='list_babies'),

    #Departure paths
    path('departures/', views.list_departures, name='list_departures'),
    path('departures/add/', views.add_departure, name='add_departure'),
    path('departures/<int:departure_id>/', views.view_departure, name='view_departure'),
    path('departures/<int:departure_id>/edit/', views.edit_departure, name='edit_departure'),
    path('departures/<int:departure_id>/delete/', views.delete_departure, name='delete_departure'),

    #Doll-type paths
    path('doll_types/', views.list_doll_types, name='list_doll_types'),
    path('doll_types/add/', views.add_doll_type, name='add_doll_type'),
    path('doll_types/<int:doll_type_id>/', views.view_doll_type, name='view_doll_type'),
    path('doll_types/<int:doll_type_id>/edit/', views.edit_doll_type, name='edit_doll_type'),
    path('doll_types/<int:doll_type_id>/delete/', views.delete_doll_type, name='delete_doll_type'),

    #Doll paths
    path('dolls/', views.list_dolls, name='list_dolls'),
    path('dolls/add/', views.add_doll, name='add_doll'),
    path('dolls/<int:doll_id>/', views.view_doll, name='view_doll'),
    path('dolls/<int:doll_id>/edit/', views.edit_doll, name='edit_doll'),
    path('dolls/<int:doll_id>/delete/', views.delete_doll, name='delete_doll'),

    #Sales paths
    path('sales/', views.list_sales, name='list_sales'),
    path('sales/add/', views.add_sales, name='add_sales'),
    path('sales/<int:sales_id>/', views.view_sales, name='view_sales'),
    path('sales/<int:sales_id>/edit/', views.edit_sales, name='edit_sales'),
    path('sales/delete/<int:sales_id>/', views.delete_sales, name='delete_sales'),

    #Babypayment paths
    path('babypayments/', views.babypayments_list, name='babypayments_list'),
    path('add_babypayment/', views.add_babypayment, name='add_babypayment'),
    path('babypayments/<int:babypayment_id>/', views.view_babypayment, name='view_babypayment'),
    path('babypayments/<int:babypayment_id>/edit/', views.edit_babypayment, name='edit_babypayment'),
    path('babypayments/<int:babypayment_id>/delete/', views.delete_babypayment, name='delete_babypayment'),

    #Sitterpayment paths
    path('sitterpayments/', views.sitterpayments_list, name='sitterpayments_list'),
    path('add_sitter_payment/', views.add_sitter_payment, name='add_sitter_payment'),
    path('sitterpayments/<int:sitterpayment_id>/', views.view_sitterpayment, name='view_sitterpayment'),
    path('sitterpayments/<int:sitterpayment_id>/edit/', views.edit_sitterpayment, name='edit_sitterpayment'),
    path('sitterpayments/<int:sitterpayment_id>/delete/', views.delete_sitterpayment, name='delete_sitterpayment'),

    #Item paths
    path('items/', views.list_items, name='list_items'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/<int:item_id>/', views.view_item, name='view_item'),
    path('items/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),

   #Stock paths
    path('stock/', views.list_stock, name='list_stock'),
    path('stock/add/', views.add_stock, name='add_stock'),
    path('stock/<int:stock_id>/', views.view_stock, name='view_stock'),
    path('stock/edit/<int:stock_id>/', views.edit_stock, name='edit_stock'),
    path('stock/delete/<int:stock_id>/', views.delete_stock, name='delete_stock'),

    #Issuing paths
    path('issuing/', views.list_issuing, name='list_issuing'),
    path('issuing/add/', views.add_issuing, name='add_issuing'),
    path('issuing/<int:issuing_id>/', views.view_issuing, name='view_issuing'),
    path('issuing/<int:issuing_id>/edit/', views.edit_issuing, name='edit_issuing'),
    path('issuing/<int:issuing_id>/delete/', views.delete_issuing, name='delete_issuing'),
    

]
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    