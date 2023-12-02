from django.contrib import admin

from order_app.models import Order, OrderFood


@admin.action(description='Set selected orders delivered')
def set_delivered(modeladmin , request, queryset):
    queryset.update(status='delivered')


@admin.action(description='Set selected orders not delivered')
def set_notdelivered(modeladmin, request, queryset):
    queryset.update(status='not delivered')

class OrderAdmin(admin.ModelAdmin):
    actions = [set_delivered , set_notdelivered]
    list_display = ['telegram_user', 'total_price', 'description', 'lat', 'lon', 'delivered_by', 'status']
    search_fields = ['telegram_user', 'delivered_by']
    list_filter = ['status']
    fieldsets = [
        ('General Information', {
            'fields': ('total_price', 'telegram_user', 'lat', 'lon', 'delivered_by', 'status', 'delivered_at', 'description')
        })
    ]

class OrderFoodAdmin(admin.ModelAdmin):
    list_display = ['order', 'food', 'price' , 'amount']
    list_display_links = ['order', 'food']
    search_fields = ['order', 'food']

    fieldsets = [
        (
            'Main Infromations',
            {
                'fields': ['order', 'food', 'price', 'amount']
            }
        )
    ]



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderFood, OrderFoodAdmin)