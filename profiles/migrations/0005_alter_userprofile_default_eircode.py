# Generated by Django 4.2.16 on 2025-01-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_rename_full_name_userprofile_default_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_eircode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
