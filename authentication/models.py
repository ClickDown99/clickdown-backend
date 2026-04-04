from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.IntegerField(("ID"), primary_key=True)
    username = models.CharField(("Username"), max_length=100, unique=True)
    email = models.EmailField(("Email"), max_length=254, unique=True)
    password = models.CharField(("Password"), max_length=100)
    first_name = models.CharField(("First Name"), max_length=50)
    last_name = models.CharField(("Last Name"), max_length=50)
    is_active = models.BooleanField(("Is Active"))
    date_joined = models.DateTimeField(("Date joined"), auto_now=False, auto_now_add=False)
    team = models.ManyToManyField("tasks.Team", verbose_name=("Teams"))