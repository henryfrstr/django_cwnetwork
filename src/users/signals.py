from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile, Relationship
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Relationship)
def add_to_friends(sender, instance, **kwargs):
    sender_ = instance.sender
    receiver_  = instance.receiver
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()
