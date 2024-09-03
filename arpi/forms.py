# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'gmail', 'username', 'password1', 'password2']
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# class CustomUser(AbstractUser):
#     # Other custom fields here

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',  # Custom related name for groups
#         blank=True,
#         help_text='The groups this user belongs to.',
#         verbose_name='groups',
#     )

#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_set',  # Custom related name for user permissions
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
