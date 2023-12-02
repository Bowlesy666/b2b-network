# Generated by Django 3.2.23 on 2023-11-20 04:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0004_auto_20231120_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateField(help_text='Date when the review was created.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='profile_reviewed',
            field=models.ForeignKey(help_text='User profile being reviewed.', on_delete=django.db.models.deletion.CASCADE, related_name='profile_reviewed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_from',
            field=models.ForeignKey(help_text='User profile giving the review.', on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_from', to='userprofile.userprofile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(help_text='Rating given in stars (1 to 5).', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.TimeField(help_text='Time when the review was created.'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='alternative_company_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Alternative contact number for the company.', max_length=128, null=True, region='GB', unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='business_sector',
            field=models.CharField(choices=[('other', 'Other...'), ('accounting', 'Accounting'), ('analytics', 'Analytics & Market Research'), ('construction', 'Construction'), ('education', 'Education'), ('energy', 'Oil, Gas & Electricity'), ('energy_renewable', 'Renewable Energy'), ('engineering', 'Engineering'), ('estate_agent', 'Estate Agency'), ('entrepreneur', 'Entrepreneur'), ('finance', 'Finance'), ('food', 'Food Production'), ('health_care', 'Health Care'), ('hospitality', 'Hospitality'), ('insurance', 'Insurance'), ('law', 'Law'), ('logistics', 'Transport & Logistics'), ('management', 'Management'), ('manufacturing', 'Manufacturing'), ('marketing', 'Marketing'), ('management_consulting', 'Management Consulting'), ('recruitment', 'Recruitment Agency'), ('retail', 'Retail'), ('technology', 'Technology'), ('telecomms', 'IT & Telecommunication'), ('warehouse', 'Warehousing & Operations')], default='other', help_text='Select the business sector for the user.', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Primary contact number for the company.', max_length=128, region='GB', unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Contact number for the user.', max_length=128, region='GB', unique=True),
        ),
    ]
