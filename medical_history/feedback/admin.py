from django.contrib import admin
from .models import Feedback
from django.contrib.auth.models import User, Group
# Register your models here.


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['record', 'email', 'date', 'issue', 'reporting_officer']
    #list_display_links = ['reporting_officer', 'record']
    list_filter = ['record', 'date', 'email']

    # def has_add_permission(self, request):
    #   return False


admin.site.register(Feedback, GeneralAdmin)

# unregistering User and Group

admin.site.unregister(User)
admin.site.unregister(Group)
