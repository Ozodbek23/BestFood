from rest_framework import serializers

from food_app.models import Category, Food


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'




class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['updated_at', 'created_at']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        exclude = ['updated_at', 'created_at']


