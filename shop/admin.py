from django.contrib import admin
from . models import *
# Register your models here.

class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,categadmin)

class proadmin(admin.ModelAdmin):
    list_display = ['name','slug','img','price','stock','available']
    list_editable = ['img','price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(products,proadmin)