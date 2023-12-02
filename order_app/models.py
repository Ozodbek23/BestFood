from django.db import models
from users_app.models import TelegramUser, User
from food_app.models import Food


class StatusChoice(models.TextChoices):
    DELIVERED = ('delivered',)
    NOT_DELIVERED = ('not delivered',)


class Order(models.Model):
    total_price = models.IntegerField()
    telegram_user = models.ForeignKey(TelegramUser, related_name='telegram_user_order', on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    delivered_by = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE)
    status = models.CharField(max_length=125, choices=StatusChoice.choices)
    foods = models.ManyToManyField(Food, related_name='order_food', through="OrderFood")
    delivered_at = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.telegram_user} {self.delivered_by}"


class OrderFood(models.Model):
    order = models.ForeignKey(Order, related_name='Order_orderfood', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='food_orderfood', on_delete=models.CASCADE)
    price = models.IntegerField()
    amount = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order_food'

    def __str__(self):
        return f"{self.food} {self.price}"
