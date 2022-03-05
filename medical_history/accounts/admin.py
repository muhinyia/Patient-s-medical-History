from django.contrib import admin
from .models import HealthOfficer
from django.contrib.auth.models import User
# Register your models here.


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['reg_number', 'user',
                    'id_number', 'phone', 'email', 'title', 'facility', ]
    list_display_links = ['reg_number']
    list_filter = ['facility', 'title']

    # def has_add_permission(self, request):
    #   return False


admin.site.register(HealthOfficer, GeneralAdmin)

# unregistering User and Group

# admin.site.unregister(User)
