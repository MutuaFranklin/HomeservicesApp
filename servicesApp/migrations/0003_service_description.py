# Generated by Django 3.2.7 on 2021-09-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesApp', '0002_alter_service_service_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
