from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations =True

    #   Customizing authentcaton by email instead of username(so dis s a custom user model thing)
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password,**extrafields):
        extrafields.setdefault('is_superuser', True)
        if extrafields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password,**extrafields)


class UserData(AbstractBaseUser, PermissionsMixin):
    username = None
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        return self.name
                        