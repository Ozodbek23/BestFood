from django import forms

from order_app.models import Order, OrderFood


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'total_price': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram_user': forms.Select(attrs={'class': 'form-control'}),
            'lat': forms.NumberInput(attrs={'class': 'form-control'}),
            'lon': forms.NumberInput(attrs={'class': 'form-control'}),
            'delivered_by': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'foods': forms.Select(attrs={'class': 'form-control'}),
            'delivered_at': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }



class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        fields = '__all__'
        widgets = {
            'order': forms.Select(attrs={'class': 'form-control'}),
            'food': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }
