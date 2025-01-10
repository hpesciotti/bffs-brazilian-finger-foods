from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_eircode = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9]{3}[A-Za-z0-9]{4}$',
                message="Enter a valid Eircode (e.g., A65F4E2).",
            )
        ],
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Check if the profile exists before saving
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()