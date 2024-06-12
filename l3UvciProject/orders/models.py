from django.db import models
from products.models import Product
from users.models import User


class CartItem(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"

class Cart(models.Model):
    
    session_key = models.CharField(max_length=40, primary_key=True)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Panier pour {self.user}"

    def get_total_price(self):
        """
        Calcule le prix total du panier.
        """
        total = 0
        for item in self.items.all():
            total += item.product.price * item.quantity
        return total


class Order(models.Model):
    ORDER_STATUS = [
        ('pending', 'En attente de confirmation'),
        ('confirmed', 'Confirmée'),
        ('processing', 'En cours de traitement'),
        ('shipped', 'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
        ('refunded', 'Remboursée'),
        ('exchanged', 'Échangée'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Remplacez 'auth' par le nom de votre application d'authentification si elle est différente
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_STATUS,default="pending")
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    