# Generated by Django 3.2.23 on 2023-11-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_alter_userprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.TextField(max_length=200, null=True, unique=True),
        ),
    ]
