# Generated by Django 4.0.4 on 2022-05-18 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_company_name_alter_job_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='seniority',
        ),
    ]
