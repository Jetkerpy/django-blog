

from django.contrib.auth.admin import UserAdmin

from django.contrib import admin

from .forms import CustomUserCreationForm, CustomChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age']



admin.site.register(CustomUser, CustomUserAdmin)