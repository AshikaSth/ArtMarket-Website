from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=False)
    is_artist = models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_gallery=models.BooleanField(default=False)
    

    def __str__(self):
            return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio=models.TextField(blank=True)
    website = models.URLField(blank=True)
    profile_picture = models.URLField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Social_links(models.Model): 
    platform = models.CharField(max_length=50)
    url= models.URLField(unique=True) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')

    def __str__(self):
        return f"{self.profile.user.username}'s {self.platform} Link"