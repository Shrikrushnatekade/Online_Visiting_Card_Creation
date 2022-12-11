from django.contrib import admin
from .models import SelfCard
# Register your models here.
# admin.site.register(SelfCard)
@admin.register(SelfCard)
class selfcardAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'userimg','date']

