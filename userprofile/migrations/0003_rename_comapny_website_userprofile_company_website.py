# Generated by Django 3.2.23 on 2023-11-20 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20231120_0332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='comapny_website',
            new_name='company_website',
        ),
    ]
