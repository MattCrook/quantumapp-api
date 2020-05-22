from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):

    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    username = models.CharField(null=True, blank=True, max_length=50)
    owner_email = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(null=True, blank=True, max_length=50)
    picUrl = models.ImageField(null=True, blank=True)
    rollerCoaster_credits = models.ManyToManyField("RollerCoaster", through="Credit" )

    class Meta:
        verbose_name = ("userProfile")
        verbose_name_plural = ("userProfiles")
        # ordering = (F('user.date_joined').asc(nulls_last=True),)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# @receiver(post_save, sender=User)
# def create_userProfile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# # Every time a `User` is saved, its matching `profile`
# # object will be saved.
# @receiver(post_save, sender=User)
# def save_userProfile(sender, instance, **kwargs):
#     instance.userProfile.save()
