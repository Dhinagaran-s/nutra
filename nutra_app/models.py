from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class CustomUser(AbstractUser):
    user_type_choices = ((1,'Admin'),(2,'Developer'),(3,'ApiUsers'))
    user_type = models.CharField(default=1, max_length=20, choices=user_type_choices)


class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username



class DeveloperUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    auth_token = models.TextField()
    verify_token = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username





class ApiUsersUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    auth_token = models.TextField()
    verify_token = models.TextField()
    req_per_day = models.IntegerField(default=100)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username






@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    if instance.user_type == 1:
        AdminUser.objects.create(admin=instance)
    if instance.user_type == 2:
        DeveloperUser.objects.create(admin=instance)
    if instance.user_type == 3:
        ApiUsersUser.objects.create(admin=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminuser.save()
    if instance.user_type == 2:
        instance.developeruser.save()
    if instance.user_type == 3:
        instance.apiusersuser.save()
        





















