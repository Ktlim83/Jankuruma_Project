from django.contrib import admin
from .models import ContactUser


# Register your models here.
class ContactUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(ContactUser, ContactUserAdmin)



