# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# # class CustomUser(AbstractUser):
# #     gmail = models.EmailField(unique=True)
# #     first_name = models.CharField(max_length=50)
# #     last_name = models.CharField(max_length=50)
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     # Your custom fields, if any
#     pass


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Your custom fields, if any
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # This avoids the clash with auth.User
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # This avoids the clash with auth.User
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

