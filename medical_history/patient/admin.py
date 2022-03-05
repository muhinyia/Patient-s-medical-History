from django.contrib import admin
from .models import Patient, PatientBio


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['huduma_id', 'first_name',
                    'last_name', 'gender', 'dob', 'phone', 'county']
    list_display_links = ['huduma_id']
    list_filter = ['huduma_id', 'dob', 'gender', 'county']

    # def has_add_permission(self, request):
    #   return False


admin.site.register(PatientBio, GeneralAdmin)


class GeneralAdmin2(admin.ModelAdmin):
    list_display = ['patient', 'facility', 'health_officer',
                    'date', 'diagnosis_made', 'treatment_offered']
    list_display_links = ['patient', 'facility', ]
    list_filter = ['health_officer', 'diagnosis_made', 'treatment_offered']


admin.site.register(Patient, GeneralAdmin2)

# unregistering User and Group

# admin.site.unregister(User)
