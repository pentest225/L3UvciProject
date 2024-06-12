from django.db import models
import json 
from django.contrib.postgres.fields import ArrayField
from users.models import User,Artisan
from django.core.validators import MinValueValidator, MaxValueValidator

class ProductCategory(models.Model):
    name = models.CharField()
    description = models.TextField()
    icon = models.CharField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.name}'

class ProductSubCategory(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    artisan = models.ForeignKey(Artisan,on_delete=models.CASCADE)
    name = models.CharField()
    description = models.TextField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.name}'
    
# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE)
    name = models.CharField()
    description = models.TextField()
    main_image = models.URLField()
    big_image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.PositiveIntegerField() 
    return_delay = models.PositiveIntegerField()
    warranty_period = models.IntegerField(help_text="Warranty period in months")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
      

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.URLField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=7)
    color_name = models.CharField(blank=True,null=True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.name}'
    

class ProductAdditionalInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    info_key = models.CharField()
    info_value = models.CharField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f'{self.info_key} : {self.info_value}'
    

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Rating between 0 and 5")

    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    

class UserProductFavorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    





    
    