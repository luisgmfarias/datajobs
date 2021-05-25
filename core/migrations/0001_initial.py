# Generated by Django 3.2.3 on 2021-05-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=25)),
                ('job_title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=70)),
                ('remote', models.CharField(max_length=6)),
                ('workplace', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
