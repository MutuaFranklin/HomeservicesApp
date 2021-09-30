# Generated by Django 3.2.7 on 2021-09-26 11:41

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Profile Pic')),
                ('gender', models.TextField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')])),
                ('mobile', models.CharField(blank=True, max_length=18)),
                ('home_location', models.CharField(blank=True, max_length=50)),
                ('current_location', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True, default='Readily available')),
                ('main_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_service', to='servicesApp.service')),
                ('secondary_service_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_one', to='servicesApp.service')),
                ('secondary_service_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_two', to='servicesApp.service')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
