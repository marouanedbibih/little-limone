from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser,PermissionsMixin # type: ignore
from .manager import UserManager

class User(AbstractUser,PermissionsMixin):
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    ROLE_CHOICES = [
        ('admin','ADMIN'),
        ('user','USER'),
    ]
    
    username = models.CharField(max_length=50,unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='user')
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = UserManager()
    
    # Add related_name to avoid conflict with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom reverse accessor for 'groups'
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Custom reverse accessor for 'user_permissions'
        blank=True,
    )
    
    def __str__(self) -> str:
            return f"{self.first_name} {self.last_name} has role {self.role} with email {self.email} and username {self.username}"    
        

        