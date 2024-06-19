from django.contrib import admin
from .models import ProductCategory,ProductSubCategory,ProductImage,ProductColor,ProductAdditionalInfo,Product,ProductReview,UserProductFavorite

admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
admin.site.register(ProductAdditionalInfo)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(UserProductFavorite)
# Register your models here.
