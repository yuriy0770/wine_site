
from django.db import models
from main.models import Product
from users.models import CustomUser

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Корзина {self.user.username}'  # ИСПРАВИЛ

    def get_total_price(self):  # ДОБАВИЛ (пригодится)
        total = 0
        for item in self.items.all():
            total += item.product.price * item.count
        return total

    def get_total_quantity(self):  # ДОБАВИЛ
        total = 0
        for item in self.items.all():
            total += item.count
        return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)  # вместо quantity, тоже норм

    def __str__(self):
        return f'{self.count} x {self.product.name}'  # ИСПРАВИЛ

    def get_total_price(self):  # ДОБАВИЛ
        return self.product.price * self.count