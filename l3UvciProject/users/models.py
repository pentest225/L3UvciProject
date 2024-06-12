from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('artisan', 'Artisan'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artisan_profile')
    sector = models.CharField(max_length=255)  # Secteur d'activité
    bio = models.TextField(null=True, blank=True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    

    def __str__(self):
        return f'{self.user.username} - {self.sector}'


class Newslatter(models.Model):
    emial = models.EmailField(max_length=254)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    
    
    
class ContactUs(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    