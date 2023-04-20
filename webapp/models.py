from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create extended User Profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name='followed_by', blank=True, symmetrical=False)
    bio = models.TextField(max_length=2000, blank=True)
    profile_text = models.CharField(max_length=200, blank=True)
    last_seen = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username


# Create a new profile when a new user is created and use receiver decorator to save the profile from the instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        UserProfile.save(instance)
        # User follows themselves at creation
        instance.userprofile.follows.add(instance.userprofile)
