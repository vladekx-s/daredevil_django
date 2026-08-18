from django.db import models
from django.utils.text import slugify   

class User(models.Model):
    # id, name, username, email, password, avatar, watched_list
    ...
    
    
class Resource(models.Model):
    # source, name, slug, created_at, description
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    main_image = models.ImageField(upload_to='resources/main')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return self.name