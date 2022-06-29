from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Team(models.Model):
    ﬁrst_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    role = models.CharField(max_length=50, blank=False)
    twitter = models.CharField(max_length=50, default='#', blank=True)
    facebook = models.CharField(max_length=50, default='#', blank=True)
    instagram = models.CharField(max_length=50, default='#', blank=True)
    linkedin = models.CharField(max_length=50, default='#', blank=True)
    image = models.ImageField(upload_to='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # def image_tag(self):
    #     return mark_safe('<img src="/%s"  class="img-fluid" alt="" />' % (self.image))