from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for CustomUser model.
    Extends Django's default UserAdmin to include custom fields.
    """
    
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    
    # Fields to filter by in the admin sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_of_birth')
    
    # Fields to search in the admin interface
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Ordering of users in the list view
    ordering = ('username',)
    
    # Fieldsets for the user detail/edit page
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
            'description': 'Custom fields for extended user information'
        }),
    )
    
    # Fieldsets for adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )


# Register CustomUser with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
