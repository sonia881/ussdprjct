from django.contrib import admin
from .models import *
# Register your models here.

class HahaAdmin (admin.ModelAdmin):
    list_display =[ 'phoneNumber, names']
    search_fields =['names']

admin.site.register(Haha, HahaAdmin)
