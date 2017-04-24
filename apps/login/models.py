from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def login(self,loginData):
        messages = []
        if len(loginData['email']) < 1:
            messages.append("Email is Empty!")
        if not EMAIL_REGEX.match(loginData['email']):
            messages.append("Invalid email!")
        if len(loginData['password']) < 1:
            messages.append("Password is Empty!")
        return messages
    def verify(self, loginData):
        messages = []
        if not User.objects.filter(email=loginData['email']):
            messages.append("Invalid User!")
        else:
            if loginData['password'] != User.objects.get(email=loginData['email']).password:
                messages.append("Invlaid password")
        return messages
    def register(self, postData):
        messages = []
        if len(postData['first_name']) < 1:
            messages.append("First name needs to be greater than 2!")
        if len(postData['last_name']) < 1:
            messages.append("Last name needs to be greater than 2!")
        if len(postData['email']) < 1:
            messages.append("email needs to be greater field!")
        if not EMAIL_REGEX.match(postData['email']):
            messages.append("Invalid email!")
        if len(postData['password']) < 1:
            messages.append("Passowrd must be field!")
        if postData['conf_password'] != postData['password']:
            messages.append("Password not match!")
        return messages
class User(models.Model):
    first_name = models.CharField(max_length = 225)
    last_name = models.CharField(max_length = 225)
    email = models.CharField(max_length = 225)
    password = models.CharField(max_length = 225)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
