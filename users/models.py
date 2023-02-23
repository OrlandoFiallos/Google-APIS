from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    tiemstamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    address = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=8, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    
    captcha_score = models.FloatField(default=0.0)
    has_profile = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user}'
    