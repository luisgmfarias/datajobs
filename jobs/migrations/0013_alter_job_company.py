# Generated by Django 4.0.4 on 2022-05-24 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_company_glassdoor_alter_company_linkedin_and_more'),
        ('jobs', '0012_remove_job_company_name_job_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company'),
        ),
    ]
