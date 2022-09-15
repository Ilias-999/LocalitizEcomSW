from django.contrib import admin
from .models import Category, OrderItem, Product, Order, Review, Contact

admin.site.register(Category)
admin.site.register(Product)

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
    ('Product', {'fields':['product'],}),
    ('Quantity', {'fields':['quantity'],}),
    ('Price', {'fields':['price'],}),               
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0
    
@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'emailAddress', 'created']
    list_display_links = ['id', 'emailAddress', 'created']
    search_fields = ['id', 'emailAddress', 'created']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created']
    
    fieldsets = [
        
        ('ORDER INFORMATION', {'fields':['id', 'token','total','created','emailAddress']}),
              
    ]

    inlines = [
    OrderItemAdmin,
    ]
    
    def has_delete_permission(self, request, obj= None):
        return False
    
    def has_add_permission(self, request):
        return False
    

admin.site.register(Review)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']

admin.site.register(Contact, ContactAdmin)

