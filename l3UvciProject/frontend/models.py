from django.db import models

# Create your models here.


class AppAssert(models.Model):
    app_icon = models.URLField()
    app_name = models.CharField(max_length=255)
    app_description = models.TextField()
    is_active = models.BooleanField(default=True)
    app_primary_color = models.CharField(max_length=7) # La couleur principale de l'application
    
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.sector}'


class AppSocialLink(models.Model):
    social_icon = models.CharField()
    social_name = models.CharField()
    social_link = models.CharField()
    
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.social_name}'
    

class ContactInfo(models.Model):
    place = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    email = models.EmailField()
    phone = models.CharField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    
    
class BannerSection(models.Model):
    banner_image = models.URLField()
    banner_title = models.CharField()
    banner_description = models.CharField()
    banner_font_color = models.CharField(max_length=7) # La couleur de font de la banier
    is_header_banner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    link_action = models.URLField() #Le lien de l'action 

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True,blank=True)
    
    
    def __str__(self):
        return f'{self.banner_title}'

    
    
    
    
    
    