from django.db import models
from django.contrib.auth.models import User, Group
from facilities.models import Facility

# Create your models here.


class HealthOfficer(models.Model):
    titles = (
        ('Medical Oficer', 'Medical Officer'),
        ('Consultant', 'Consultant'),
        ('Surgeon', 'Surgeon'),
        ('Neural Surgeon', 'Neural Surgeon'),
        ('Gynaecologist', 'Gynaecologist'),
        ('ENT Expert', 'ENT Expert'),
        ('Paediatric', 'Paediatric'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Clinical Officer', 'Officer'),
        ('Cardiologist', 'Cardiologist'),
        ('Other', 'Other')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=10, unique=True)
    reg_number = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100, choices=titles)
    facility = models.ForeignKey(Facility, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    pic = models.ImageField(
        blank=True, upload_to='media/officers/%Y/%m/%d', help_text='Health officers Profile Pic')

    def __str__(self) -> str:
        return self.reg_number

    class Meta:
        db_table = 'health_officers'
        ordering = ('reg_number',)
        verbose_name_plural = 'health_officers'
