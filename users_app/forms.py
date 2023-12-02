from django import forms

from users_app.models import User, TelegramUser


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'})
        }




class TelegramUserForm(forms.ModelForm):
    class Meta:
        model = TelegramUser
        fields = "__all__"
        widgets = {
            'chate_id': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'is_blocked': forms.TextInput(attrs={'class': 'form-control'})
        }