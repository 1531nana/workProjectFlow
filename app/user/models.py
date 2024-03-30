from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
  username = models.CharField(max_length = 255, unique = True)
  email = models.EmailField(max_length = 255, unique = True)
  password = models.CharField(max_length = 130)
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'password']

  class Meta: # Agregar metadatos
    db_table = 'users'
        
  def __str__(self):
    return "{}".format(self.username)