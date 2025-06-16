from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','is_theater_manager','is_approved','otp','otp_verify')