from django.db import models
from django.utils.text import slugify   
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biography = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.username
    
    
    class Meta:
        ordering = ['-date_joined']
    
    
class Episodes(models.Model):
    season = models.PositiveSmallIntegerField()
    episode = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)  
          
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        #               Как "%.2d" в С
        return f"{self.season:02d}:{self.episode:02d} - {self.title}"
    
    class Meta:
        ordering = ['-season', '-episode']
        
        
class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episodes, on_delete=models.CASCADE)
    progress = models.PositiveSmallIntegerField(default=0)
    watched_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.episode}"
    
    class Meta:
        ordering = ['-watched_at']