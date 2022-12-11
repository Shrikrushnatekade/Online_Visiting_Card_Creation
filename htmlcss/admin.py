from csv import list_dialects
from django.contrib import admin
from .models import Member, Profile
# Register your models here.
# from .models import User


@admin.register(Member)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','funame','email','mobile']

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'token', 'verify']