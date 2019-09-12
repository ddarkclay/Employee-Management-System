from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=False, blank=False)
    salary = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='picture/%Y/%m/%d/' ,max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-salary',)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(profile__designation="Admin")

class Employee(User):
    class Meta:
        ordering = ('first_name',)
        proxy = True

    objects = EmployeeManager()

    def full_name(self):
        return self.first_name + " - " + self.last_name

@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
    
