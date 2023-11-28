from django.contrib import admin
from Fast.models import UserDetails

# Register your models here.


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('u_id',
                    'u_fname',
                    'u_lname',
                    'u_contact',
                    'u_address',
                    'u_email',
                    'u_password',
                    'is_admin',
                    'otp',
                    'otp_used')


# Alternative of @admin.register() Decorator
# admin.site.register(UserDetails, UserDetailsAdmin)
