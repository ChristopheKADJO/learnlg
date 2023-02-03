from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.
"""
    The MyUserManager class extends Django's BaseUserManager
    and provides custom methods for creating users and superusers.
"""
class MyUserManager(BaseUserManager):
    def create_user(self, email, firstname, password=None):
        user = self.model(
            email=self.normalize_email(email).lower().strip(),
            firstname=firstname.strip().title()
        )
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, firstname, password=None):
        user = self.create_user(email=email, firstname=firstname, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
    
    
"""
    The CustomUser class extends AbstractBaseUser and defines fields for storing user information, as well as methods for checking user permissions. The USERNAME_FIELD is set to email, and the REQUIRED_FIELDS is set to ['firstname'].
"""
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    firstname = models.CharField(max_length=30, blank=False)
    
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)    
    is_admin = models.BooleanField(default=False, null=False)    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname']
    objects = MyUserManager()
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True