import email
from tabnanny import verbose
from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.TextField(
        max_length=20, blank=False, unique=True, verbose_name='name'
    )
    first_name = models.TextField(max_length=30, verbose_name='firstname')
    last_name = models.TextField(max_length=30, verbose_name='surename')
    email_addr = models.EmailField(
        blank=False, unique=True, verbose_name='email')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
