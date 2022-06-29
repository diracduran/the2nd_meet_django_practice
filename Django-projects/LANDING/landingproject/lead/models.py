from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    subject = models.CharField(max_length=50, blank=False)
    message = models.TextField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)