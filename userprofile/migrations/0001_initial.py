# Generated by Django 3.2.23 on 2023-11-20 01:19

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('business_sector', models.CharField(choices=[('other', 'Other...'), ('accounting', 'Accounting'), ('analytics', 'Analytics & Market Research'), ('construction', 'Construction'), ('education', 'Education'), ('energy', 'Oil, Gas & Electricity'), ('energy_renewable', 'Renewable Energy'), ('engineering', 'Engineering'), ('estate_agent', 'Estate Agency'), ('entrepreneur', 'Entrepreneur'), ('finance', 'Finance'), ('food', 'Food Production'), ('health_care', 'Health Care'), ('hospitality', 'Hospitality'), ('insurance', 'Insurance'), ('law', 'Law'), ('logistics', 'Transport & Logistics'), ('management', 'Management'), ('manufacturing', 'Manufacturing'), ('marketing', 'Marketing'), ('management_consulting', 'Management Consulting'), ('recruitment', 'Recruitment Agency'), ('retail', 'Retail'), ('technology', 'Technology'), ('telecomms', 'IT & Telecommunication'), ('warehouse', 'Warehousing & Operations')], default='other', max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('comapny_website', models.URLField()),
                ('company_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='GB', unique=True)),
                ('alternative_company_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='GB', unique=True)),
                ('company_contact_email', models.EmailField(max_length=254, unique=True)),
                ('company_bio', models.TextField()),
                ('company_services_post', models.TextField()),
                ('company_hero_picture', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('user_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='GB', unique=True)),
                ('display_user_email', models.BooleanField(default=True)),
                ('user_about', models.TextField()),
                ('user_profile_img', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_created', models.DateField()),
                ('time_created', models.TimeField()),
                ('profile_reviewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_reviewed', to='userprofile.userprofile')),
                ('review_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_from', to='userprofile.userprofile')),
            ],
        ),
    ]
