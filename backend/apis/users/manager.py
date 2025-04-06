
from django.contrib.auth.models import BaseUserManager # type: ignore

class UserManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,password=None,**extra_fields):
        if email is None:
            raise ValueError('The Email is required')
        if username is None:
            raise ValueError('The Username is required')
        if first_name is None:
            raise ValueError('The First Name is required')
        if last_name is None:
            raise ValueError('The Last Name is required')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,first_name,last_name,password=None,**extra_fields):
        if email is None:
            raise ValueError('The Email is required')
        if username is None:
            raise ValueError('The Username is required')
        if first_name is None:
            raise ValueError('The First Name is required')
        if last_name is None:
            raise ValueError('The Last Name is required')
        
        admin = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            role='admin',
            **extra_fields,
        )
        
        admin.set_password(password)
        admin.save()
        return admin