from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request


# Create your models here.

class Profile(models.Model):
    key = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=50,null=True)
    job = models.CharField(max_length=100,null=True,default='___',blank=True)
    bio = models.CharField(max_length=500,null=True)
    followers = models.ManyToManyField(User, related_name='followers_ofUser')
    following = models.ManyToManyField(User, related_name='following_ofUser')
    account_created = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='user_profile',default='user_profile/default_profile2.png')

    def __str__(self):
        return(self.name)

    def num_followers(self):
        return self.followers.all().count()

    def num_following(self):
        return self.following.all().count()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        prof = Profile.objects.create(user=instance,name=f"{instance.first_name} {instance.last_name}")
        prof.save()


