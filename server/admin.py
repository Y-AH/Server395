from django.contrib import admin

# Register your models here.
from server import models


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')


admin.site.register(models.Contact, ContactAdmin)