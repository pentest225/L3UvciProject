from django.contrib import admin
from .models import User,Artisan,Newslatter,ContactUs
# Register your models here.
admin.site.register(User)
admin.site.register(Artisan)
admin.site.register(Newslatter)
admin.site.register(ContactUs)