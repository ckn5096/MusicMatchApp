#import self as self
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomUser(User):

    def __str__(self):
        return self.username
