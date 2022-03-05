# Generated by Django 3.2.4 on 2021-07-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_patient_docs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='docs',
            field=models.FileField(blank=True, help_text='Treatment Support Documents', upload_to='media/patients/treatment documents/%Y/%m/%d'),
        ),
    ]
