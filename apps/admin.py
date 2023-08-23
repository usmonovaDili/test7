from django.contrib import admin
from .models import User
from .forms import UserForms

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForms
    list_display = ['id','name']

