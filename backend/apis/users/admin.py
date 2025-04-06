from django.contrib import admin # type: ignore

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email','role','is_active']
    list_filter = ['role','is_active']
    search_fields = ['username','first_name','last_name','email']
    ordering = ['id']
    fieldsets = (
        (None,{'fields':('username','first_name','last_name','email','password')}),
        ('Permissions',{'fields':('role','is_active')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('username','first_name','last_name','email','password1','password2','role','is_active'),
        }),
    )
    filter_horizontal = ()

