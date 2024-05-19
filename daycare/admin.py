from django.contrib import admin
from .models import *

# Register your models here.
class SitterpaymentAdmin(admin.ModelAdmin):
    list_display = ('s_name', 'date', 'baby_count', 'amount', 'total_amount')
 
class StockAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'purchased_on', 'quantity_bought', 'quantity_issued_out', 'available_stock_display')

    def available_stock_display(self, obj):
        return obj.available_stock

    available_stock_display.short_description = 'Available Stock'

class SalesAdmin(admin.ModelAdmin):
    list_display = ('doll', 'b_name', 'quantity_sold', 'unit_price', 'comp_total', 'received_amount', 'comp_balance', 'date_sold')

    def comp_total(self, obj):
        return obj.comp_total

    def comp_balance(self, obj):
        return obj.comp_balance

    comp_total.short_description = 'Total'
    comp_balance.short_description = 'Balance'

admin.site.register(Sales, SalesAdmin)

admin.site.register(Stock, StockAdmin) 
admin.site.register(Sitterpayment, SitterpaymentAdmin)
admin.site.register(Sitter)
admin.site.register(Baby)
admin.site.register(Staytype)
admin.site.register(Item)
admin.site.register(Sitterattendance)
admin.site.register(Departure)
admin.site.register(Doll_type)
admin.site.register(Doll)
admin.site.register(Babypayment)
admin.site.register(Issuing)

