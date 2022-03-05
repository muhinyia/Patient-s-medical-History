from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('details/', views.get_patient, name='get_patient'),
    path('details/record=<int:record_id>', views.get_record, name='get_record'),
    path('details/main/patient=<int:id>',
         views.get_patient_back, name='get_patient_back'),
    path('record', views.enter_record, name='enter_record'),
    path('add/', views.add_patient, name='add_patient'),
]
