# Generated by Django 3.2.4 on 2021-06-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('facility_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('is_public', models.BooleanField(default=True)),
                ('is_registered', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'health_facilities',
                'db_table': 'health_facility',
                'ordering': ('facility_no',),
            },
        ),
    ]
