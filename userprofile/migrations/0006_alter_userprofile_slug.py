# Generated by Django 3.2.23 on 2023-11-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20231120_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]