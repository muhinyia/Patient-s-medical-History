from django.urls import path
from . import views

app_name = 'admins'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_physician/', views.add_doc, name='add_doc'),
    path('add_facility/', views.add_facility, name='add_facility'),
    path('patients/', views.get_patients, name='get_patients'),
    path('physicians/', views.get_docs, name='get_docs'),
    path('feedback/', views.get_feedbacks, name='get_feedbacks'),
    path('medical_records/', views.get_records, name='get_records'),
    path('health_facilities/', views.get_facilities, name='get_facilities'),







]
