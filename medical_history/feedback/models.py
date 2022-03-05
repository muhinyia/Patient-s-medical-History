from django.db import models
from patient.models import Patient
from accounts.models import HealthOfficer
# Create your models here.


class Feedback(models.Model):
    email = models.EmailField()
    record = models.ForeignKey(Patient, on_delete=models.CASCADE)
    issue = models.TextField()
    reporting_officer = models.ForeignKey(
        HealthOfficer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
