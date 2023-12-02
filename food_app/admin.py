from django.contrib import admin

from food_app.models import Food, Category


@admin.action(description='Activate selected foods')
def set_active(modeladmin , request, queryset):
    queryset.update(is_active=True)

@admin.action(description="Disactivate selected foods")
def set_disactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


class FoodAdmin(admin.ModelAdmin):
    actions = [set_active, set_disactivate]
    list_display = ['name' , 'description', 'price', 'image', 'is_active']
    list_display_links = ['name', 'description', 'image']
    search_fields = ['name', 'price', 'description']
    list_filter = ['is_active']

    fieldsets = [
        (
            'Foods main informations',
            {
                'fields':['name', 'description', 'price']
            }
        ),
        (
            "Foods additional informations",
            {
                'fields':['image','category']
            }
        ),
        (
            "Foods status",
            {
                'fields':['is_active']
            }
        )
    ]



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']






admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)