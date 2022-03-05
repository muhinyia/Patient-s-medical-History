from .models import Facility
from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['facility_no', 'name',
                    'county', 'city', 'phone', 'is_public', 'is_registered']
    list_display_links = ['name']
    list_filter = ['is_public']

    # def has_add_permission(self, request):
    #   return False


admin.site.register(Facility, GeneralAdmin)

# unregistering User and Group

# admin.site.unregister(User)
