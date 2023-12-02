from rest_framework import serializers

from order_app.models import Order, OrderFood


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
        
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['updated_at']


class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = "__all__"

class OrderFoodDetailSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        exclude = ['updated_at']
