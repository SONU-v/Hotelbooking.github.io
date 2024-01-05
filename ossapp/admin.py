from django.contrib import admin
from . models import Customer
#class AdminProduct(admin.ModelAdmin):
#    list_display= ['name','price','desc','category']

# Register your models here.



class AdminCustomer(admin.ModelAdmin):
    list_display = [ 'checkin','checkout','name','age','person','phone1','phone2','email','address','gender','selectcity','selectstate']
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Customer,AdminCustomer)
