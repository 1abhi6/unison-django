from django.contrib import admin
from contact.models import contactData

# Register your models here.


class contactAdmin(admin.ModelAdmin):
    list_display = ['name', 'contactNum', 'email', 'message']


admin.site.register(contactData, contactAdmin)
