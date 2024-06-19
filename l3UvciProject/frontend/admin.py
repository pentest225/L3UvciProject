from django.contrib import admin
from .models import AppAssert,AppSocialLink,BannerSection
# Register your models here.

admin.site.register(AppSocialLink)
admin.site.register(AppAssert)
admin.site.register(BannerSection)