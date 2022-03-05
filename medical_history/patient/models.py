from accounts.models import HealthOfficer
from django.db import models
from django.db.models.fields import DateField
from facilities.models import Facility


class PatientBio(models.Model):

    counties = (
        ('Mombasa', 'Mombasa'),
        ('Kwale', 'Kwale'),
        ('Kilifi', 'Kilifi'),
        ('Tana River', 'Tana River'),
        ('Lamu', 'Lamu'),
        ('Taita Taveta', 'Taita Taveta'),
        ('Garissa', 'Garissa'),
        ('Wajir', 'Wajir'),
        ('Mandera', 'Mandera'),
        ('Marsabit', 'Marsabit'),
        ('Isiolo', 'Isiolo'),
        ('Meru', 'Meru'),
        ('Tharaka Nithi', 'Tharaka Nithi'),
        ('Embu', 'Embu'),
        ('Kitui', 'Kitui'),
        ('Machakos', 'Machakos'),
        ('Makueni', 'Makueni'),
        ('Nyandarua', 'Nyandarua'),
        ('Nyeri', 'Nyeri'),
        ('Kirinyaga', 'Kirinyaga'),
        ("Murang'a", "Murang'a"),
        ('Kiambu', 'Kiambu'),
        ('Turkana', 'Turkana'),
        ('West Pokot', 'West Pokot'),
        ('Samburu', 'Samburu'),
        ('Trans-Nzoia', 'Trans-Nzoia'),
        ('Uasin Gishu', 'Uasin Gishu'),
        ('Elgeyo Marakwet', 'Elgeyo Marakwet'),
        ('Nandi', 'Nandi'),
        ('Baringo', 'Baringo'),
        ('Laikipia', 'Laikipia'),
        ('Nakuru', 'Nakuru'),
        ('Narok', 'Narok'),
        ('Kajiado', 'Kajiado'),
        ('Kericho', 'Kericho'),
        ('Bomet', 'Bomet'),
        ('Kakamega', 'Kakamega'),
        ('Vihiga', 'Vihiga'),
        ('Bungoma', 'Bungoma'),
        ('Busia', 'Busia'),
        ('Siaya', 'Siaya'),
        ('Kisumu', 'Kisumu'),
        ('Homa Bay', 'Homa Bay'),
        ('Migori', 'Migori'),
        ('Kisii', 'Kisii'),
        ('Nyamira', 'Nyamira'),
        ('Nairobi', 'Nairobi'),

    )
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    huduma_id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #other_name = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(
        max_length=10, help_text='for infants, enter gurdians/parents phone')
    #email = models.EmailField(blank=True)
    gender = models.CharField(
        max_length=50,  choices=genders)
    #location = models.CharField(max_length=100)
    #constituency = models.CharField(max_length=100)
    county = models.CharField(max_length=50, choices=counties)
   # pic = models.ImageField(
   #     blank=True, upload_to='media/patients/profile_pics/%Y/%m/%d', help_text="Patient's Profile Pic")

    def __str__(self) -> str:
        return self.huduma_id

    class Meta:
        db_table = 'patientbio'
        ordering = ('dob',)
        verbose_name_plural = 'patientbio'


class Patient(models.Model):
    patient = models.ForeignKey(PatientBio, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.DO_NOTHING)
    health_officer = models.ForeignKey(
        HealthOfficer, on_delete=models.DO_NOTHING)
    date = models.DateField(
        auto_now_add=True, help_text='The Date this Record was made')
    presenting_symptoms = models.TextField()
    lab_works = models.TextField()
    diagnosis_made = models.TextField()
    treatment_offered = models.TextField()
    comment = models.TextField()
    x_ray = models.ImageField(
        blank=True, upload_to='media/patients/x_rays/%Y/%m/%d', help_text="Patient's Profile Pic")
    # other_docs HERE ATTACH ANY OTHER RELEVANT DOCUMENTS
    docs = models.FileField(
        blank=True, upload_to='media/patients/treatment documents/%Y/%m/%d', help_text="Treatment Support Documents")

    class Meta:
        db_table = 'patientinfo'
        ordering = ('date',)
        verbose_name_plural = 'patientinfo'

    def __str__(self) -> str:
        return str(self.id)
