from django.db import models

# Create your models here.


class Facility(models.Model):

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
    levels = (
        ('Level 1', 'Level 1'),
        ('Level 2', 'Level 2'),
        ('Level 3', 'Level 3'),
        ('Level 4', 'Level 4'),
        ('Level 5', 'Level 5'),
        ('Level 6', 'Level 6'),
    )

    facility_no = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    county = models.CharField(
        max_length=50,  choices=counties, default='Nairobi')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    is_public = models.BooleanField(default=True)
    is_registered = models.BooleanField(default=True)
    # give the choices for a hospital level
    facility_level = models.CharField(
        max_length=50,  choices=levels, default='Level 1')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'health_facility'
        ordering = ('facility_no',)
        verbose_name_plural = 'health_facilities'
