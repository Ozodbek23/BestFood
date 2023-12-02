from django.contrib import admin

from users_app.models import TelegramUser, User


@admin.action(description='Set selected users admin')
def set_admin(modeladmin, request, queryset):
    queryset.update(role='ADMIN')


@admin.action(description='Set selected users operator')
def set_operator(modeladmin, request, queryset):
    queryset.update(role='OPERATOR')


@admin.action(description='Set selected users deliver')
def set_deliver(modeladmin, request, queryset):
    queryset.update(role='DELIVER')


class UserAdmin(admin.ModelAdmin):
    actions = [set_admin, set_deliver, set_operator]
    list_display = ['first_name', 'last_name', 'role']
    list_display_links = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    list_filter = ['role']





@admin.action(description='Block selected telegram users')
def set_active(modeladmin , request, queryset):
    queryset.update(is_blocked=True)

@admin.action(description="Unblock selected telegram users")
def set_disactivate(modeladmin, request, queryset):
    queryset.update(is_blocked=False)


class TelegramUserAdmin(admin.ModelAdmin):
    actions = [set_active , set_disactivate]
    list_display = ['full_name', 'phone_number', 'chat_id', 'is_blocked']
    list_display_links = ['full_name', 'phone_number']
    search_fields = ['full_name']
    list_filter = ['is_blocked']


admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(User, UserAdmin)
