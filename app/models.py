from django.contrib.auth.models import User
from django.db.models import Model, ImageField, CharField, OneToOneField
from django.db import models


class Person(Model):
    profile_picture = ImageField(upload_to="profile_pictures", blank=True, null=True)
    user = OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    phone_number = CharField(max_length=15, blank=True, null=True)
    hiring_date = models.DateField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
