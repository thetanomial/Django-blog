from django.db import models
from django.contrib.auth.models import (
    AbstractUser, BaseUserManager)


class UserRole(models.TextChoices):
    MODERATOR = "moderator", "Moderator"
    CREATOR = "creator", "Creator"
    VIEWER = "viewer", "Viewer"




class UserManager(BaseUserManager):
    def create_user(self,email,name,password=None,**extra_fields):
        if not email:
            raise ValueError(
                "The email field must be set."
            )
        email = self.normalize_email(email)
        user = self.model(email=email,name=name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)


        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, name, password, **extra_fields)




class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)  # Django handles password hashing

    username = None  # Remove username field

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    # user manager
    objects = UserManager()

    def __str__(self):
        return self.email
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.VIEWER)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"