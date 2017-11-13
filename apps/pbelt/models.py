from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "User name should be more than 5 characters"
        if len(postData['username']) < 10:
            errors["username"] = "User-name should be more than 5 characters"
        if len(postData['password']) < 10:
            errors["password"] = "password should be more than 5 characters"
        
        return errors;
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Appointment(models.Model):
    friend = models.ForeignKey(User,related_name="attending")
    appointment= models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()