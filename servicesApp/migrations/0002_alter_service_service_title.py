# Generated by Django 3.2.7 on 2021-09-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_title',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]