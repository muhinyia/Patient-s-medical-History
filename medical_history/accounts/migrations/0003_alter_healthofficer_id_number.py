# Generated by Django 3.2.4 on 2021-07-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210623_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthofficer',
            name='id_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
